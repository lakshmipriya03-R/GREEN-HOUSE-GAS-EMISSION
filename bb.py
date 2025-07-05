import streamlit as st
import pandas as pd
import os

st.title("Greenhouse Gas Emission Factor Model Training")

# Debug info: show current directory and files
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

try:
    # Load dataset directly from local file — update filename exactly as your file
    df = pd.read_excel("greenhouse_data.xlsx")
    st.success("Dataset loaded successfully!")
    st.write(df.head())

    # Your further processing here...

except FileNotFoundError:
    st.error("Dataset file 'greenhouse_data.xlsx' not found in the current directory!")



