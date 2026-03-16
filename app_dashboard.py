# from flask import Flask, render_template
# import pandas as pd
# from collections import Counter
# from datetime import datetime
# import json

# app = Flask(__name__)

# @app.route("/")
# def dashboard():

#     df = pd.read_csv("data/news_final_output.csv")

#     total_articles = int(len(df))

#     # Load real accuracy
#     try:
#         with open("data/model_accuracy.txt", "r") as f:
#             accuracy = float(f.read())
#     except:
#         accuracy = 0

#     # Sentiment Distribution
#     sentiment_counts = df["sentiment_label"].value_counts()
#     sentiment_labels = json.dumps(list(sentiment_counts.index))
#     sentiment_values = json.dumps([int(x) for x in sentiment_counts.values])

#     # Trending Words
#     all_words = " ".join(df["processed_text"].astype(str)).split()
#     word_freq = Counter(all_words)
#     top_words = [(word, int(count)) for word, count in word_freq.most_common(5)]

#     sample_data = df[["Title", "sentiment_label"]].head(4).to_dict(orient="records")

#     return render_template(
#         "dashboard.html",
#         total_articles=total_articles,
#         accuracy=accuracy,
#         date=datetime.now().strftime("%d-%m-%Y"),
#         top_words=top_words,
#         sentiment_labels=sentiment_labels,
#         sentiment_values=sentiment_values,
#         sample_data=sample_data
#     )

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, render_template
# import pandas as pd
# import json
# from collections import Counter
# from datetime import datetime

# app = Flask(__name__)

# @app.route("/")
# def dashboard():

#     df = pd.read_csv("data/news_final_output.csv")

#     total_articles = len(df)

#     with open("model_accuracy.txt", "r") as f:
#         accuracy = f.read().split(":")[1].strip().replace("%","")

#     date = datetime.now().strftime("%Y-%m-%d")

#     words = " ".join(df["processed_text"].astype(str)).split()

#     word_freq = Counter(words)

#     top_words = word_freq.most_common(10)

#     keyword_labels = [word for word, count in top_words]
#     keyword_values = [count for word, count in top_words]

#     sentiment_counts = df["sentiment_label"].value_counts()

#     sentiment_labels = json.dumps(list(sentiment_counts.index))
#     sentiment_values = json.dumps([int(x) for x in sentiment_counts.values])

#     sample_data = df[["Title","sentiment_label"]].head(5).to_dict(orient="records")

#     return render_template(
#         "dashboard.html",
#         total_articles=total_articles,
#         accuracy=accuracy,
#         date=date,
#         top_words=top_words,
#         sample_data=sample_data,
#         sentiment_labels=sentiment_labels,
#         sentiment_values=sentiment_values,
#         keyword_labels=json.dumps(keyword_labels),
#         keyword_values=json.dumps(keyword_values)
#     )


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template
# import pandas as pd
# import json
# from collections import Counter
# from datetime import datetime
# import os

# app = Flask(__name__)

# @app.route("/")
# def dashboard():

#     # Load dataset
#     df = pd.read_csv("data/news_final_output.csv")

#     total_articles = len(df)

#     # -----------------------------
#     # MODEL ACCURACY SAFE LOADING
#     # -----------------------------
#     if os.path.exists("model_accuracy.txt"):
#         with open("model_accuracy.txt","r") as f:
#             accuracy = f.read().split(":")[1].strip().replace("%","")
#     else:
#         accuracy = "72.22"   # fallback accuracy

#     date = datetime.now().strftime("%Y-%m-%d")

#     # -----------------------------
#     # TRENDING KEYWORDS
#     # -----------------------------
#     words = " ".join(df["processed_text"].astype(str)).split()

#     word_freq = Counter(words)

#     top_words = word_freq.most_common(10)

#     keyword_labels = [w for w,c in top_words]
#     keyword_values = [c for w,c in top_words]

#     # -----------------------------
#     # SENTIMENT DISTRIBUTION
#     # -----------------------------
#     sentiment_counts = df["sentiment_label"].value_counts()

#     sentiment_labels = list(sentiment_counts.index)
#     sentiment_values = [int(x) for x in sentiment_counts.values]

#     # -----------------------------
#     # SAMPLE DATA
#     # -----------------------------
#     sample_data = df[["Title","sentiment_label"]].head(5).to_dict(orient="records")

#     return render_template(
#         "dashboard.html",
#         total_articles=total_articles,
#         accuracy=accuracy,
#         date=date,
#         top_words=top_words,
#         sample_data=sample_data,
#         keyword_labels=json.dumps(keyword_labels),
#         keyword_values=json.dumps(keyword_values),
#         sentiment_labels=json.dumps(sentiment_labels),
#         sentiment_values=json.dumps(sentiment_values)
#     )


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, session
import pandas as pd
import json
from collections import Counter
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "newspulse_secret_key"

USERNAME = "admin"
PASSWORD = "1234"


# ---------------- LOGIN ROUTE ----------------

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# ---------------- DASHBOARD ROUTE ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    # Load dataset
    df = pd.read_csv("data/news_final_output.csv")

    total_articles = len(df)

    # ---------------- SAFE ACCURACY READING ----------------
    accuracy = "0"

    if os.path.exists("data/model_accuracy.txt"):

        with open("data/model_accuracy.txt") as f:

            content = f.read().strip()

            if ":" in content:
                accuracy = content.split(":")[1].replace("%","").strip()
            else:
                accuracy = content.replace("%","").strip()

    # ---------------- DATE ----------------
    date = datetime.now().strftime("%Y-%m-%d")

    # ---------------- KEYWORD EXTRACTION ----------------
    words = " ".join(df["processed_text"].astype(str)).split()

    word_freq = Counter(words)

    top_words = word_freq.most_common(10)

    keyword_labels = [w for w,c in top_words]
    keyword_values = [c for w,c in top_words]

    # ---------------- SENTIMENT COUNTS ----------------
    sentiment_counts = df["sentiment_label"].value_counts()

    sentiment_labels = list(sentiment_counts.index)
    sentiment_values = [int(x) for x in sentiment_counts.values]

    # ---------------- SAMPLE DATA ----------------
    sample_data = df[["Title","sentiment_label"]].head(5).to_dict(orient="records")

    return render_template(
        "dashboard.html",
        total_articles=total_articles,
        accuracy=accuracy,
        date=date,
        top_words=top_words,
        sample_data=sample_data,
        keyword_labels=json.dumps(keyword_labels),
        keyword_values=json.dumps(keyword_values),
        sentiment_labels=json.dumps(sentiment_labels),
        sentiment_values=json.dumps(sentiment_values)
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)