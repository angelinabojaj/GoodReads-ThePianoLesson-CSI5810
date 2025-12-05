# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import spacy # pip install spacy

# Data
goodreads_generated = "GoodReads-Reviews-File.csv"
goodreads_thepianolesson = pd.read_csv(goodreads_generated, encoding="latin1")

# Task 1
def task1_page():
    st.title("Task 1")
    st.subheader("Observe and document frequently used tags that users use to describe The Piano Lesson.")
    st.text("Findings")
    
    nlp = spacy.load("en_core_web_sm")
    
    tags = goodreads_thepianolesson["Tags"].dropna().astype(str) # Drops all "None"
    
    all_tags =[]
    
    for entry in tags:
        unfiltered_tags = entry.split(",")
        
        for tag in unfiltered_tags:
            tag = tag.strip().lower()
            if not tag:
                continue
            
            processing_tag_spacy = nlp(tag)
            
            lemmas = [
                    token.lemma_.lower()
                      for token in processing_tag_spacy
                      if not token.is_stop and not token.is_punct and token.lemma_.strip()]
            
            if lemmas:
                normalized_tags = " ".join(lemmas)
                all_tags.append(normalized_tags)
        
    count_tags = pd.Series(all_tags).value_counts().reset_index()
    count_tags.columns = ["tag", "count"]
    
    # Output Tags
    st.write("# Most Frequency Tags Sorted Using spaCy")
    st.dataframe(count_tags.head(20))
    
    # Plotting spaCy Results
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(count_tags["tag"].head(15), count_tags["count"].head(15))
    ax.set_title("Most Frequency Tags - According to spaCy")
    ax.set_ylabel("Count")
    ax.set_xticklabels(count_tags["tag"].head(15), rotation = 50, ha="right")     
    st.pyplot(fig)
            