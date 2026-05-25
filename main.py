import pandas as pd
import ast

#Load datasets
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

#Merge
movies = movies.merge(credits, on='title')

#Select needed columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#Remove null values
movies.dropna(inplace=True)

#Convert stringified JSON to list
def convert(text):
    return [i['name'] for i in ast.literal_eval(text)]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

#Get top 3 cast
def convert_cast(text):
    L = []
    for i in ast.literal_eval(text)[:3]:
        L.append(i['name'])
    return L

movies['cast'] = movies['cast'].apply(convert_cast)

#Get director
def fetch_director(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return i['name']
    return ''

movies['crew'] = movies['crew'].apply(fetch_director)

#Combine all features into tags
movies['tags'] = movies['overview'] + " " + movies['genres'].astype(str) + " " + movies['keywords'].astype(str) + " " + movies['cast'].astype(str) + " " + movies['crew']

#Keep final columns
new_df = movies[['movie_id','title','tags']]

#Lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

print("✅ Data Preprocessing Done")
print(new_df.head())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vectors)

print("✅ Similarity Matrix Created")

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    print("\n🎬 Recommended Movies:\n")
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

#Testing
recommend("Avatar")

import pickle

pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Model Saved Successfully")
