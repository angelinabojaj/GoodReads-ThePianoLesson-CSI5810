# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
def home():
    st.title("CSI 5810: GoodReads The Piano Lesson App")
    st.subheader("Introduction")
    st.text("Welcome to my application demonstrating data relevant to predicting...")
    st.set_page_config(initial_sidebar_state="expanded")
    plt.close("all")
    st.session_state.page = "home"

# Side Bar Navigation
# st.sidebar.title("Graphs")
# st.sidebar.button("Home Page", key = "home", on_click=home)
# st.sidebar.button("Atomic Mass", key = "mass", on_click=go_mass)
# st.sidebar.button("FIE", key = "fie", on_click=go_fie)