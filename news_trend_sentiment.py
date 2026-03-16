# ===============================================
# NewsPulse - Milestone 3
# Trend Detection & Sentiment Analysis
# ===============================================

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob

print("\n===== Milestone 3 - Trend Detection & Sentiment Analysis =====\n")

# -----------------------------------------------
# STEP 1: LOAD DATA
# -----------------------------------------------
file_path = "data/news_with_sentiment.csv"
df = pd.read_csv(file_path)

print("Total Articles Loaded:", len(df))

# -----------------------------------------------
# STEP 2: REMOVE DUPLICATES
# -----------------------------------------------
before = len(df)
df = df.drop_duplicates(subset="Title")
after = len(df)

print("Duplicates Removed:", before - after)

# -----------------------------------------------
# STEP 3: TF-IDF TREND DETECTION
# -----------------------------------------------
vectorizer = TfidfVectorizer(max_features=20)
X = vectorizer.fit_transform(df["processed_text"])

feature_names = vectorizer.get_feature_names_out()
mean_scores = np.mean(X.toarray(), axis=0)

top_indices = mean_scores.argsort()[-10:][::-1]

trending_keywords = [feature_names[i] for i in top_indices]

print("\nTop 10 Trending Keywords (TF-IDF):")
for word in trending_keywords:
    print("-", word)

# -----------------------------------------------
# STEP 4: FREQUENCY BASED TREND (COUNTER)
# -----------------------------------------------
all_words = " ".join(df["processed_text"]).split()
word_freq = Counter(all_words)

print("\nTop 5 Frequent Words (Counter):")
top_frequent = word_freq.most_common(5)
for word, count in top_frequent:
    print(word, ":", count)

# -----------------------------------------------
# STEP 5: SENTIMENT SCORE + LABEL
# -----------------------------------------------
df["sentiment_score"] = df["processed_text"].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

def label_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["sentiment_score"].apply(label_sentiment)

sentiment_counts = df["sentiment_label"].value_counts()

print("\nSentiment Distribution:")
print(sentiment_counts)

# -----------------------------------------------
# STEP 6: SAVE FINAL OUTPUT
# -----------------------------------------------
df.to_csv("data/news_final_output.csv", index=False)

print("\nFinal processed file saved: data/news_final_output.csv")

print("\n===== Milestone 3 Backend Completed Successfully =====")