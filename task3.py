# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

# Data
goodreads_generated = "GoodReads-Reviews-File.csv"
goodreads_thepianolesson = pd.read_csv(goodreads_generated, encoding="latin1")

def task3_page():
    st.title("Task 3")
    st.subheader("Predicting the reviews of future readers of The Piano Lesson.")
    st.text("Findings")
    
    X =['reviews']
    Y =['rating'].astype(int)
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,Y, test_size=0.2, random_state=42
    )
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
        ('model', RandomForestClassifier(n_estimators=350))
    ])
    
    # Predictions
    pipeline.fit(X_train, Y_train)
    predictions = pipeline.predict(X_test)
    
    # Accuracy & Accuracy Scores
    print("Acucuracy:", accuracy_score(Y_test, predictions))
    print(classification_report(Y_test, predictions))