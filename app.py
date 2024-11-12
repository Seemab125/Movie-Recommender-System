import streamlit as st
import pickle
import pandas as pd

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    Recommended_movies = []
    for i in movies_list:
        Recommended_movies.append(movies.iloc[i[0]].title)
    return Recommended_movies


# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit title and custom styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7f6;
        }
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: 600;
            color: #FFFFFF;
            margin-top: 50px;
        }
        .description {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 40px;
        }
        .recommendation {
            font-size: 22px;
            color: #333;
            margin-top: 30px;
            text-align: center;
            font-weight: 500;
        }
        .movie-list {
            list-style-type: none;
            padding: 0;
        }
        .movie-item {
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            font-size: 18px;
            font-weight: 500;
            color: #333;
            transition: transform 0.3s ease;
        }
        .movie-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .container {
            padding: 40px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 900px;
            margin: auto;
        }
        .selectbox {
            width: 100%;
            padding: 15px;
            font-size: 18px;
            background-color: #f5f6fa;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .recommend-button {
            background-color: #6C63FF;
            color: white;
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
            margin-top: 20px;
        }
        .recommend-button:hover {
            background-color: #5748e2;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Find your next favorite movie by getting recommendations based on your choice!</div>', unsafe_allow_html=True)

# Create a container for the interface
with st.container():
    # Movie selection dropdown
    selected_movie_name = st.selectbox(
        'Select a Movie:',
        movies['title'].values,
        key="movie_select",
        help="Choose a movie to get recommendations",
        label_visibility="visible",
        index=0,
        format_func=lambda x: x if len(x) <= 40 else x[:37] + '...'
    )

    # Button to get recommendations
    recommend_button = st.button('Recommend', key="recommend_button", help="Click to get movie recommendations", use_container_width=True)

    # If the button is pressed, show recommendations
    if recommend_button:
        Recommendations = recommend(selected_movie_name)
        
        st.markdown('<div class="recommendation">🎬 Recommended Movies</div>', unsafe_allow_html=True)
        st.markdown('<ul class="movie-list">', unsafe_allow_html=True)
        for movie in Recommendations:
            st.markdown(f'<li class="movie-item">{movie}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
