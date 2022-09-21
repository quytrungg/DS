import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def preProcess(df, labels, test_size, randome_state):
    x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
    return x_train,x_test,y_train,y_test

def passiveAgressiveClassifier():

    return

def main():
    df = pd.read_csv('news.csv')

    # replace first column's name with 'id'
    df.rename(columns={'Unnamed: 0':'id'}, inplace=True)

    # initial props
    colName = df.columns
    labels = df.label
    shape = df.shape

    # display DataFrame
    print(shape)
    print(df.head(10))
    
    # x_train,x_test,y_train,y_test = preProcess(df, labels, test_size=0.9, randome_state=7)
    
    # tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
    # #DataFlair - Fit and transform train set, transform test set
    # print(x_train.loc[6237])
    # tfidf_train=tfidf_vectorizer.fit_transform(x_train.loc[6237]) 
    # print('sdlkf', tfidf_train)