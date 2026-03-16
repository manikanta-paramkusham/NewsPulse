
import requests
import csv
import pandas as pd


API_KEY = "69efd416a6364e298e90e65b5d6b6a2e"

url = "https://newsapi.org/v2/everything"

params = {
    "q": "news",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 100,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("Error fetching news. Status Code:", response.status_code)
    exit()

data = response.json()
articles = data.get("articles", [])

if not articles:
    print("No news articles found.")
    exit()

print("\n===== Milestone 1 - NewsPulse Project =====")
print("\nTop 5 News Headlines:\n")

for i, article in enumerate(articles[:5], start=1):
    print(f"{i}. {article.get('title')}")

# =========================
# SAVE TO CSV
# =========================
file_path = "data/news_data.csv"

with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Source", "Published Date"])

    for article in articles:
        writer.writerow([
            article.get("title"),
            article.get("source", {}).get("name"),
            article.get("publishedAt")
        ])

total_fetched = len(articles)

print(f"\nTotal articles fetched: {total_fetched}")
print("News data saved to data/news_data.csv")

# =========================
# LOAD CSV
# =========================
df = pd.read_csv(file_path)

# -------------------------
# COUNT BEFORE CLEANING
# -------------------------
before_cleaning = len(df)

# -------------------------
# DATA CLEANING
# -------------------------
df = df.dropna()
df = df.drop_duplicates(subset="Title")
df["Title"] = df["Title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)

# -------------------------
# COUNT AFTER CLEANING
# -------------------------
after_cleaning = len(df)

cleaned_file_path = "data/news_data_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

print("Cleaned data saved to data/news_data_cleaned.csv")

# 🔹 These two lines added exactly below Total articles fetched section
print(f"\nTotal Articles Before Cleaning: {before_cleaning}")
print(f"Total Articles After Cleaning : {after_cleaning}")

# =========================
# DISPLAY CLEANED DATA
# =========================
print("\nSample Cleaned News Data:\n")
print(df.head())

# =========================
# MINI USE CASE
# =========================
print("\nMini Use Case Results:")
print("Total News Articles:", after_cleaning)
print("Unique News Sources:", df["Source"].nunique())

print("\n===== Milestone 1 Completed Successfully =====")







































# import requests
# import csv
# import pandas as pd


# API_KEY = "69efd416a6364e298e90e65b5d6b6a2e"

# url = "https://newsapi.org/v2/everything"

# params = {
#     "q": "news",              
#     "language": "en",
#     "sortBy": "publishedAt",
#     "pageSize": 100,          
#     "apiKey": API_KEY
# }

# response = requests.get(url, params=params)

# if response.status_code != 200:
#     print("Error fetching news. Status Code:", response.status_code)
#     exit()

# data = response.json()
# articles = data.get("articles", [])

# if not articles:
#     print("No news articles found.")
#     exit()

# print("\n===== Milestone 1 - NewsPulse Project =====")
# print("\nTop 5 News Headlines:\n")

# for i, article in enumerate(articles[:5], start=1):
#     print(f"{i}. {article.get('title')}")

# file_path = "data/news_data.csv"

# with open(file_path, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Source", "Published Date"])

#     for article in articles:
#         writer.writerow([
#             article.get("title"),
#             article.get("source", {}).get("name"),
#             article.get("publishedAt")
#         ])

# print(f"\nTotal articles fetched: {len(articles)}")
# print("News data saved to data/news_data.csv")


# df = pd.read_csv(file_path)

# df = df.dropna()
# df = df.drop_duplicates(subset="Title")
# df["Title"] = df["Title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)

# cleaned_file_path = "data/news_data_cleaned.csv"
# df.to_csv(cleaned_file_path, index=False)

# print("Cleaned data saved to data/news_data_cleaned.csv")


# print("\nSample Cleaned News Data:\n")
# print(df.head())


# print("\nMini Use Case Results:")
# print("Total News Articles:", len(df))
# print("Unique News Sources:", df["Source"].nunique())

# print("\n===== Milestone 1 Completed Successfully =====")






















# import sys
# import requests
# import csv
# import pandas as pd

# # =========================
# # STEP 1: API CONFIGURATION
# # =========================
# API_KEY = "69efd416a6364e298e90e65b5d6b6a2e"

# URL = "https://newsapi.org/v2/everything"

# PARAMS = {
#     "q": "news",
#     "language": "en",
#     "sortBy": "publishedAt",
#     "pageSize": 100,
#     "apiKey": API_KEY
# }

# # =========================
# # STEP 2: FETCH NEWS
# # =========================
# response = requests.get(URL, params=PARAMS)

# if response.status_code != 200:
#     print(f"Error fetching news. Status Code: {response.status_code}")
#     sys.exit()

# data = response.json()
# articles = data.get("articles", [])

# if not articles:
#     print("No news articles found.")
#     sys.exit()

# print("\n===== Milestone 1 - NewsPulse Project =====")
# print("\nTop 5 News Headlines:\n")

# for index, article in enumerate(articles[:5], start=1):
#     print(f"{index}. {article.get('title')}")

# print(f"\nTotal articles fetched: {len(articles)}")

# # =========================
# # STEP 3: SAVE TO CSV
# # =========================
# file_path = "data/news_data.csv"

# with open(file_path, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Source", "Published Date"])

#     for article in articles:
#         writer.writerow([
#             article.get("title"),
#             article.get("source", {}).get("name"),
#             article.get("publishedAt")
#         ])

# print("News data saved to data/news_data.csv")

# # =========================
# # STEP 4: LOAD CSV
# # =========================
# df = pd.read_csv(file_path)

# # =========================
# # STEP 5: DATA CLEANING
# # =========================
# df = df.dropna()
# df = df.drop_duplicates(subset="Title")
# df["Title"] = df["Title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)

# cleaned_path = "data/news_data_cleaned.csv"
# df.to_csv(cleaned_path, index=False)

# print("Cleaned data saved to data/news_data_cleaned.csv")

# # =========================
# # STEP 6: DISPLAY SAMPLE
# # =========================
# print("\nSample Cleaned News Data:\n")
# print(df.head())

# # =========================
# # STEP 7: MINI USE CASE
# # =========================
# print("\nMini Use Case Results:")
# print(f"Total News Articles: {len(df)}")
# print(f"Unique News Sources: {df['Source'].nunique()}")

# print("\n===== Milestone 1 Completed Successfully =====")





# import requests
# import csv
# import pandas as pd


# API_KEY = "69efd416a6364e298e90e65b5d6b6a2e"

# url = "https://newsapi.org/v2/top-headlines"

# params = {
#     "country": "us",
#     "apiKey": API_KEY
# }


# response = requests.get(url, params=params)
# data = response.json()

# articles = data.get("articles", [])

# print("Top 5 News Headlines:\n")

# for i, article in enumerate(articles[:5], start=1):
#     print(f"{i}. {article['title']}")

# file_path = "data/news_data.csv"

# with open(file_path, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Source", "Published Date"])

#     for article in articles:
#         writer.writerow([
#             article.get("title"),
#             article.get("source", {}).get("name"),
#             article.get("publishedAt")
#         ])

# print("\nNews data saved to data/news_data.csv")


# print("\nLoading data from CSV...\n")

# df = pd.read_csv("data/news_data.csv")
# print(df.head())


# df = df.dropna()
# df = df.drop_duplicates(subset="Title")
# df["Title"] = df["Title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)

# cleaned_file_path = "data/news_data_cleaned.csv"
# df.to_csv(cleaned_file_path, index=False)

# print("\nCleaned data saved to data/news_data_cleaned.csv")

# print("\nMini Use Case Results:")
# print("Total News Articles:", len(df))
# print("Unique News Sources:", df["Source"].nunique())

# import requests
# import csv
# import pandas as pd

# # =========================
# # API CONFIGURATION
# # =========================
# API_KEY = "69efd416a6364e298e90e65b5d6b6a2e"

# url = "https://newsapi.org/v2/top-headlines"

# params = {
#     "country": "us",
#     "apiKey": API_KEY
# }

# # =========================
# # FETCH NEWS
# # =========================
# response = requests.get(url, params=params)
# data = response.json()

# articles = data.get("articles", [])

# # =========================
# # SAVE TO CSV
# # =========================
# file_path = "data/news_data.csv"

# with open(file_path, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Source", "Published Date"])

#     for article in articles:
#         writer.writerow([
#             article.get("title"),
#             article.get("source", {}).get("name"),
#             article.get("publishedAt")
#         ])

# # =========================
# # LOAD CSV
# # =========================
# df = pd.read_csv("data/news_data.csv")

# # =========================
# # DATA CLEANING
# # =========================
# df = df.dropna()
# df = df.drop_duplicates(subset="Title")
# df["Title"] = df["Title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)

# df.to_csv("data/news_data_cleaned.csv", index=False)

# # =========================
# # FINAL FORMATTED OUTPUT
# # =========================
# print("\n===== Milestone 1 - NewsPulse Project =====")
# print("--------------------------------------------------")

# print("\nSample News Data:\n")

# for i, title in enumerate(df["Title"].head(5), start=1):
#     print(f"{i}. {title}")

# print("\n--------------------------------------------------")
# print(f"Total News Articles: {len(df)}")
# print(f"Unique News Sources: {df['Source'].nunique()}")

# print("\n✓ Architecture Diagram Completed")
# print("✓ News Data Collected Successfully")
# print("✓ Data Stored in CSV Format")
# print("✓ Data Cleaning Completed")
# print("✓ Mini Demo Presented")

# print("\n--------------------------------------------------")
