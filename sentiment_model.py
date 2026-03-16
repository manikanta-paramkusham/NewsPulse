import pandas as pd
import joblib
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("\n===== Training Sentiment Model =====\n")

# Load preprocessed data
df = pd.read_csv("data/news_preprocessed.csv")

# --------------------------------------
# STEP 1: Create Sentiment Labels
# --------------------------------------
def generate_label(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["processed_text"].apply(generate_label)

# Save updated file
df.to_csv("data/news_final_output.csv", index=False)

print("Sentiment labels generated.")

# --------------------------------------
# STEP 2: Prepare Data for Training
# --------------------------------------
X = df["processed_text"]
y = df["sentiment_label"]

# Check unique classes
if len(y.unique()) < 2:
    print("ERROR: Need at least 2 sentiment classes.")
    exit()

# Vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# --------------------------------------
# STEP 3: Train Model
# --------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Training Completed.")
print("Accuracy:", round(accuracy * 100, 2), "%")

# --------------------------------------
# STEP 4: Save Model + Vectorizer + Accuracy
# --------------------------------------
joblib.dump(model, "data/sentiment_model.pkl")
joblib.dump(vectorizer, "data/vectorizer.pkl")

with open("data/model_accuracy.txt", "w") as f:
    f.write(str(round(accuracy * 100, 2)))

print("Model & Accuracy Saved Successfully.")