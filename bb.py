import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Set page config
st.set_page_config(page_title="GHG Emission Predictor", layout="centered")

st.title("🌍 Greenhouse Gas Emission Predictor")

# Dropdown inputs
industry_code = st.selectbox("Select Industry Code", encoders["Industry Code"].classes_)
industry_name = st.selectbox("Select Industry Name", encoders["Industry Name"].classes_)
substance = st.selectbox("Select Substance", encoders["Substance"].classes_)
unit = st.selectbox("Select Unit", encoders["Unit"].classes_)

# Encode input
input_data = pd.DataFrame({
    "Industry Code": [encoders["Industry Code"].transform([industry_code])[0]],
    "Industry Name": [encoders["Industry Name"].transform([industry_name])[0]],
    "Substance": [encoders["Substance"].transform([substance])[0]],
    "Unit": [encoders["Unit"].transform([unit])[0]]
})

# Predict
if st.button("Predict Emission"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Emission Factor: **{prediction:.4f}**")

