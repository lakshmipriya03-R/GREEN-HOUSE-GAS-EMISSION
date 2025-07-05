
import streamlit as st
import pandas as pd
import os

st.title("Greenhouse Gas Emission Factor Model Training")

st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

try:
    df = pd.read_excel("greenhouse_data.xlsx")
    st.success("Dataset loaded successfully!")
    st.write(df.head())
except FileNotFoundError:
    st.error("Dataset file 'greenhouse_data.xlsx' not found!")




