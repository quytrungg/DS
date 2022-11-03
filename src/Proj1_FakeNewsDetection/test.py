import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('test.csv')
count = 0

train = df['text']

for i in train:
    for j in i:
        if j == ' ':
            count += 1

print(count+1)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')

tfidf_train = tfidf_vectorizer.fit_transform(train)

# print(tfidf_train)