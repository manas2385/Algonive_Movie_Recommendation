import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv('data/ratings.csv')

# Create pivot table
pivot = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Compute similarity
user_similarity = cosine_similarity(pivot)

print("✅ Collaborative model ready")