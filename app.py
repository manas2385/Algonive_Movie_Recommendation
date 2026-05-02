import streamlit as st
import pickle
import requests

# -------------------------------
# Load data
# -------------------------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# -------------------------------
# TMDb API KEY (PUT YOUR KEY HERE)
# -------------------------------
API_KEY = "fd9527ca2db0b56f1664d81e705678b1"


# -------------------------------
# Fetch Poster
# -------------------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(url)

        # Check if request worked
        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=API+Error"

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []
    reasons = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title

        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(movie_id))

        # Explanation (simple but effective)
        reasons.append(f"Shares similar genre, cast, and storyline with '{movie}'")

    return recommended_movies, recommended_posters, reasons


# -------------------------------
# UI DESIGN
# -------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 AI Movie Recommendation System")

st.markdown("""
Welcome! This system recommends movies using:
- 🎯 Content-Based Filtering  
- 🤝 User Behavior (conceptual)  
- 💬 Sentiment Insight (conceptual)

Select a movie and get personalized suggestions 👇
""")

st.divider()

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Choose a movie", movie_list)


# -------------------------------
# BUTTON ACTION
# -------------------------------
if st.button("🚀 Recommend"):

    with st.spinner("Finding best movies for you..."):

        names, posters, reasons = recommend(selected_movie)

        st.subheader("🎯 Top Recommendations")

        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                st.markdown(f"**{names[i]}**")
                st.caption(reasons[i])


# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("💡 Built using Machine Learning | Algonive Internship Project")

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    return sia.polarity_scores(text)['compound']