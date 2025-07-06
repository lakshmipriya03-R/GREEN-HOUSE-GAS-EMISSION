import streamlit as st
import pandas as pd
import joblib

# Load model + encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Helper: return real options for a column
def get_options(encoder):
    return list(encoder.classes_)

# Sidebar Title
st.sidebar.title("GHG Emission Predictor")

# Real name dropdowns
industry_code = st.sidebar.selectbox("Industry Code", get_options(encoders["Industry Code"]))
industry_name = st.sidebar.selectbox("Industry Name", get_options(encoders["Industry Name"]))
substance = st.sidebar.selectbox("Substance", get_options(encoders["Substance"]))
unit = st.sidebar.selectbox("Unit", get_options(encoders["Unit"]))
margin = st.sidebar.slider("Margin of Supply Chain Emission Factors", 0.0, 1.0, 0.05)

# Predict Button
if st.sidebar.button("Predict Emission Factor"):
    # Encode input using saved encoders
    encoded = [
        encoders["Industry Code"].transform([industry_code])[0],
        encoders["Industry Name"].transform([industry_name])[0],
        encoders["Substance"].transform([substance])[0],
        encoders["Unit"].transform([unit])[0],
        margin
    ]

    # Prediction
    prediction = model.predict([encoded])[0]

    # Show result
    st.success(f"📢 Predicted GHG Emission Factor: **{prediction:.4f}**")
    st.write("🔎 Inputs used:")
    st.write(f"- Industry Code: `{industry_code}`")
    st.write(f"- Industry Name: `{industry_name}`")
    st.write(f"- Substance: `{substance}`")
    st.write(f"- Unit: `{unit}`")
    st.write(f"- Margin: `{margin}`")



