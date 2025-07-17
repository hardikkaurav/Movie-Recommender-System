import pickle
import streamlit as st
import pandas as pd
import requests


# Function to fetch poster using TMDB movie_id
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Image"
    return full_path


# Function to recommend similar movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie, recommended_movie_posters


# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you want to recommend?',
    movies['title'].values
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)

    # Display in 5 columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            # st.text(names[i])
            st.image(posters[i])
            st.markdown(
                f"<div style='text-align: center; font-size: 14px; word-wrap: break-word;'>{names[i]}</div>",
                unsafe_allow_html=True
            )
