import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")
df = df[['title', 'genres']]

# Convert text to numbers
cv = CountVectorizer()
matrix = cv.fit_transform(df['genres'])

# Similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].title)
    
    return recommended_movies

# Streamlit UI
st.title(" Movie Recommendation System")

selected_movie = st.selectbox("Select a movie", df['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    for movie in recommendations:
        st.write(movie)