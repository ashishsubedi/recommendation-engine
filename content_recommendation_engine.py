# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
df = pd.read_csv('data.csv')
df.head()


# %%
df.shape


# %%
df.isna().sum()


# %%
df.dtypes


# %%
features = ['director','cast','duration','listed_in','description','type']


# %%
for feature in features:
    df[feature] = df[feature].fillna('')


# %%
df[features].isna().sum()


# %%
df['index'] = df.index

# %% [markdown]
# # Combine all features in one to implement count vectorizer

# %%
def combine_features(row):
    combined_features = ''
    for col in features:
        combined_features +=  row[col]+ " "
    return combined_features
    


# %%
pdf = df.copy()
pdf = pdf[features]
pdf.head()


# %%
pdf['combined'] = pdf.apply(combine_features,axis=1)


# %%
pdf['combined'].head()


# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# %%
cv = CountVectorizer()


# %%
count_matrix = cv.fit_transform(pdf['combined'])


# %%
similarity = cosine_similarity(count_matrix)


# %%
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]


# %%
movie = df.iloc[30]['title']
movie


# %%
movie_index = get_index_from_title(movie)
movie_index


# %%
similar_movies = list(enumerate(similarity[movie_index]))
sorted_similar_movies = sorted(similar_movies, key= lambda x: x[1], reverse=True)


# %%
for m in sorted_similar_movies[1:11]:
    print (get_title_from_index(m[0]))


# %%
df


# %%


