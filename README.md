# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and Machine Learning that recommends movies based on genre similarity. The project uses Flask to provide an interactive web interface with a responsive HTML and CSS design.

## 📌 Project Overview

This project recommends movies similar to a movie selected by the user. Movie genres are converted into numerical feature vectors using CountVectorizer, and Cosine Similarity is used to measure the similarity between movies.

The application is developed using Flask, allowing users to select a movie and receive the top 5 similar movie recommendations through an attractive and responsive web interface.

## ✨ Features

- 🎬 Select a movie from the available collection
- 🤖 Content-based movie recommendations
- 🔍 Genre-based similarity analysis
- ⭐ Top 5 similar movie recommendations
- 📊 Similarity score for each recommendation
- 🎨 Attractive and responsive user interface
- 📱 Mobile-friendly design
- ⚡ Fast recommendation generation

## 🧠 How It Works

The system follows these steps:

1. Load the movie dataset using Pandas.
2. Select the movie title and genre information.
3. Convert movie genres into numerical vectors using CountVectorizer.
4. Calculate similarity between movies using Cosine Similarity.
5. Identify the movies with the highest similarity scores.
6. Return the top 5 recommendations.
7. Display the results through the Flask web application.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Flask**
- **HTML5**
- **CSS3**
- **Git & GitHub**

## 📂 Project Structure

```text
movie-recommendation-flask/
│
├── app.py
├── movies.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
