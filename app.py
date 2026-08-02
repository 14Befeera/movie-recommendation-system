from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("movies.csv")

# Keep required columns
df = df[["movieId", "title", "genres"]].dropna()

# -----------------------------
# Feature Extraction
# -----------------------------
vectorizer = CountVectorizer(
    tokenizer=lambda x: x.split("|"),
    token_pattern=None
)

vectors = vectorizer.fit_transform(df["genres"])

# -----------------------------
# Similarity Calculation
# -----------------------------
similarity = cosine_similarity(vectors)


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):

    matches = df[df["title"] == movie]

    if matches.empty:
        return []

    index = matches.index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i, score in scores[1:6]:

        recommendations.append({
            "title": df.iloc[i]["title"],
            "genres": df.iloc[i]["genres"].replace("|", " • "),
            "score": round(score * 100, 1)
        })

    return recommendations


# -----------------------------
# Home Route
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    selected_movie = ""

    if request.method == "POST":

        selected_movie = request.form.get("movie", "")

        if selected_movie:
            recommendations = recommend(selected_movie)

    movies = df["title"].tolist()

    return render_template(
        "index.html",
        movies=movies,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)