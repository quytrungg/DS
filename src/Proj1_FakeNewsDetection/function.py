import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def splitData(df, labels, test_size=0.2, random_state=7):
    x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
    return x_train,x_test,y_train,y_test

def tfidfVectorizer(stop_words='english', max_df=0.7):
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    return tfidf

def passiveAgressiveClassifier(max_iter=50):
    pac = PassiveAggressiveClassifier(max_iter=50)
    return pac

def main():
    df = pd.read_csv('news.csv')
    df.rename(columns={'Unnamed: 0':'id'}, inplace=True)

    colName = df.columns
    labels = df.label
    shape = df.shape

    # print(shape)
    # print(df.head(10))
    
    x_train, x_test, y_train, y_test = splitData(df, labels)

    tfidf_vectorizer = tfidfVectorizer()

    tfidf_train = tfidf_vectorizer.fit_transform(x_train)
    tfidf_test = tfidf_vectorizer.transform(x_test)

    pac = passiveAgressiveClassifier()

    pac.fit(tfidf_train, y_train)
    y_pred = pac.predict(tfidf_test)

    score = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {round(score*100, 2)}%')
    
    print(confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))

    display = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    display.figure_.suptitle("Fake News Dectection Confusion Matrix")

    plt.show()