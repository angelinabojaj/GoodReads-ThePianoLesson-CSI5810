# Libraries
import streamlit as st # python -m streamlit run app.py
import pandas as pd
import matplotlib.pyplot as plt

# Data
goodreads_generated = "GoodReads-Reviews-File.csv"
goodreads_thepianolesson = pd.read_csv(goodreads_generated, encoding="latin1")

# Streamlit implemenation
def go_task1(): 
    plt.close("all")
    st.session_state.page = "task1"

def go_task2(): 
    plt.close("all")
    st.session_state.page = "task2"

def go_task3(): 
    plt.close("all")
    st.session_state.page = "task3"
    
def home():
    st.title("CSI 5810: GoodReads The Piano Lesson App")
    st.subheader("Introduction")
    st.text("Welcome to my application demonstrating data mined and collected from GoodReads. Specifically this application will cover the reviews for the book The Piano Lesson by August Wilsion. Provided below is the table with relevant data pertianing to the tasks undertaked in this project.")
    st.dataframe(goodreads_thepianolesson,use_container_width=True)
    st.set_page_config(initial_sidebar_state="expanded")
    plt.close("all")
    st.session_state.page = "home"

# Side Bar Navigation
st.sidebar.title("Tasks To Be Accomplishhed")
# st.sidebar.button("Intro Page", key = "task1", on_click=home)
st.sidebar.button("Task 1", key = "task1", on_click=go_task1)
st.sidebar.button("Task 2", key = "task2", on_click=go_task2)
st.sidebar.button("Task 3", key = "task3", on_click=go_task3)
st.sidebar.button("Return Home", key = "home", on_click=home)

# Loading Pages
if "page" not in st.session_state:
    home()

elif st.session_state.page == "task1":
    from task1 import task1_page
    task1_page()
    
elif st.session_state.page == "task2":
    from task2 import task2_page
    task2_page()

elif st.session_state.page == "task3":
    from task3 import task3_page
    task3_page()
    