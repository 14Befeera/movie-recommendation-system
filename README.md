#  Movie Recommendation System

This project is a content-based movie recommendation system that suggests similar movies based on genres.

##  Features
- Select a movie from dropdown
- Get top 5 similar movie recommendations
- Interactive UI using Streamlit

##  Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

##  How it Works
- Movie genres are converted into numerical vectors using CountVectorizer
- Cosine similarity is used to find similar movies
- Top 5 similar movies are recommended

##  Run the Project
```bash
streamlit run app.py

## Example

Select: Toy Story
Output: Similar animated/comedy movies
