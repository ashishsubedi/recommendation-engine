import numpy as np
import pandas as pd

import sys
import json


#Helper functions
df = pd.read_csv('titles.txt');
df['index'] = df.index

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]

title = sys.argv[1]
# title = "Chocolate"
similarity = np.load('similarity_matrix.npy')

movie_index = get_index_from_title(title)
similar_movie = list(enumerate(similarity[movie_index]))
sorted_similar_movie = sorted(similar_movie,key=lambda x: x[1],reverse=True)


results = [get_title_from_index(m[0]) for m in sorted_similar_movie[1:16]]
results = json.dumps({"result":results})
print(results)
sys.stdout.flush()

