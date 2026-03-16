# ===============================================
# NewsPulse - Milestone 2 NLP Pipeline (spaCy Version)
# ===============================================

import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob

print("\n===== Milestone 2 - NLP Processing (spaCy) =====\n")

# -----------------------------------------------
# STEP 1: LOAD CLEANED DATA
# -----------------------------------------------
file_path = "data/news_data_cleaned.csv"
df = pd.read_csv(file_path)

print("Total Articles Loaded:", len(df))

# -----------------------------------------------
# STEP 2: LOAD spaCy MODEL
# -----------------------------------------------
nlp = spacy.load("en_core_web_sm")

# -----------------------------------------------
# STEP 3: TEXT PREPROCESSING USING spaCy
# -----------------------------------------------
def preprocess_text(text):
    doc = nlp(str(text).lower())
    
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
        and token.is_alpha
        and len(token.text) > 2
    ]
    
    return " ".join(tokens)

df["processed_text"] = df["Title"].apply(preprocess_text)

df.to_csv("data/news_preprocessed.csv", index=False)

print("Text Preprocessing Completed.")

# -----------------------------------------------
# STEP 4: TF-IDF FEATURE EXTRACTION
# -----------------------------------------------
vectorizer = TfidfVectorizer(max_features=1000)
tfidf_matrix = vectorizer.fit_transform(df["processed_text"])

feature_names = vectorizer.get_feature_names_out()
mean_scores = np.mean(tfidf_matrix.toarray(), axis=0)

top_indices = mean_scores.argsort()[-10:][::-1]

print("\nTop 10 Trending Keywords:")
for index in top_indices:
    print("-", feature_names[index])

# -----------------------------------------------
# STEP 5: TOPIC MODELING (LDA)
# -----------------------------------------------
lda_model = LatentDirichletAllocation(
    n_components=3,
    random_state=42
)

lda_model.fit(tfidf_matrix)

print("\nTop 3 Topics Identified:")

for topic_idx, topic in enumerate(lda_model.components_):
    print(f"\nTopic {topic_idx + 1}:")
    
    top_indices = topic.argsort()[-8:][::-1]
    topic_words = [feature_names[i] for i in top_indices]
    
    print(", ".join(topic_words))

# -----------------------------------------------
# STEP 6: SENTIMENT ANALYSIS
# -----------------------------------------------
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["processed_text"].apply(get_sentiment)

df.to_csv("data/news_with_sentiment.csv", index=False)

# -----------------------------------------------
# STEP 7: SENTIMENT SUMMARY
# -----------------------------------------------
print("\nSentiment Distribution:")

sentiment_counts = df["sentiment"].value_counts()

for sentiment, count in sentiment_counts.items():
    print(f"{sentiment}: {count}")

print("\nTotal Articles After NLP Processing:", len(df))

print("\n===== Milestone 2 Completed Successfully =====")
