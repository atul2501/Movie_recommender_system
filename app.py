import streamlit as st
import  pickle
import pandas as pd
import requests
import gdown
import os

import requests
import time

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c38986c04eeba139e93aae724f375443&language=en-US'
    for attempt in range(5):  # Retry up to 3 times
        try:
            time.sleep(0.7)
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if not poster_path:
                return "https://via.placeholder.com/500x750?text=No+Image"
            return "https://image.tmdb.org/t/p/w500" + poster_path
        except Exception as e:
            print(f"[Attempt {attempt + 3}] Error fetching poster for movie_id {movie_id}: {e}")
    return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

#similarity = pickle.load(open('similarity.pkl','rb'))
if not os.path.exists("similarity.pkl"):
    
    gdown.download("https://drive.google.com/uc?id=1qEx0m6Dh5kjZ51UvfWuRF1e_mZW0BTr-", "similarity.pkl", quiet=False)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.header('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)

if st.button('Show Recommendation'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
