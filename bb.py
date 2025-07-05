import streamlit as st
import pandas as pd

# Your raw GitHub Excel file URL
DATA_URL = "https://raw.githubusercontent.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/main/greenhouse_gas.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_URL)
    # Clean column names: strip spaces, lowercase, replace spaces with _
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

df = load_data()

st.write("Columns in dataset:", df.columns.tolist())  # This shows the actual columns after cleaning

required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']

if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset must contain columns: {required_cols}")
    st.stop()

# Now proceed with your model training and app logic below




