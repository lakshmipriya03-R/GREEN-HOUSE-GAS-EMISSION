import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Create dropdown options from encoders (decoded values)
def get_options(enc):
    return list(enc.classes_)

# Title
st.title("🌍 GHG Emission Predictor")

# Input fields (decoded values for user-friendly display)
industry_code = st.selectbox("Industry Code", get_options(encoders["Industry Code"]))
industry_name = st.selectbox("Industry Name", get_options(encoders["Industry Name"]))
substance = st.selectbox("Substance", get_options(encoders["Substance"]))
unit = st.selectbox("Unit", get_options(encoders["Unit"]))
margin = st.number_input("Margin of Supply Chain Emission Factor", min_value=0.0)

# Predict button
if st.button("Predict Emission Factor"):
    # Encode inputs
    input_data = [
        encoders["Industry Code"].transform([industry_code])[0],
        encoders["Industry Name"].transform([industry_name])[0],
        encoders["Substance"].transform([substance])[0],
        encoders["Unit"].transform([unit])[0],
        margin
    ]
    input_df = pd.DataFrame([input_data], columns=[
        "Industry Code", "Industry Name", "Substance", "Unit", "Margins of Supply Chain Emission Factors"
    ])
    
    # Prediction
    prediction = model.predict(input_df)[0]
    st.success(f"🌿 Predicted GHG Emission Factor: {prediction:.6f}")

