import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import spacy
spacy.load("en_core_web_sm")
def get_genre(tekst):
    temp = ""
    ret = []
    for i in range(0, len(tekst)):
        if tekst[i] == " " or tekst[i] == len(tekst) - 1:
            ret.append(temp)
            temp = ""
        else:
            temp += tekst[i]
    return ret

nlp = spacy.load("en_core_web_sm")
df = pd.read_csv('imdb_top_1000.csv', sep=',')
df = df[['Genre', 'Overview', 'Meta_score']]
clean = df.dropna(axis='rows')
czas = 0
przym = 0
rzecz = 0
lengen = 1
# maxgen = 29
genres = []
for i in clean['Overview']:
    temp = get_genre(i)
    for j in temp:
        if j not in genres:
            genres.append(j)
print(genres)
for i in clean['Overview']:
    if len(i) > lengen:
        lengen = len(i)
print(lengen)
for i in clean['Overview']:
    slowa = nlp(i)
    print(slowa)






# print(clean)