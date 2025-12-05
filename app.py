# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation

def go_mass(): 
    plt.close("all")
    st.session_state.page = "atomicmass"

def go_fie(): 
    plt.close("all")
    st.session_state.page = "fie"

def go_radius(): 
    plt.close("all")
    st.session_state.page = "atomicradius"
    
def home():
    st.title("CSI 5810: GoodReads The Piano Lesson App")
    st.subheader("Introduction")
    st.text("Welcome to my application demonstrating data relevant...")
    st.set_page_config(initial_sidebar_state="expanded")
    plt.close("all")
    st.session_state.page = "home"

# Side Bar Navigation
# st.sidebar.title("Tasks To Be Accomplishhed")
# st.sidebar.button("Task 1", key = "home", on_click=home)
# st.sidebar.button("Task 2", key = "mass", on_click=go_mass)
# st.sidebar.button("Task 3", key = "fie", on_click=go_fie)

# Loading Pages
if "page" not in st.session_state:
    home()

elif st.session_state.page == "atomicmass":
    from atomicmass import atomicmass_page
    atomicmass_page()
    
elif st.session_state.page == "fie":
    from fie import fie_page
    fie_page()

elif st.session_state.page == "atomicradius":
    from atomicradius import rad_page
    rad_page()
def task1():
    return 0

def task2():
    return 0

def task3():
    return 0