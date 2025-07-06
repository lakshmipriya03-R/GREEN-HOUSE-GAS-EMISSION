import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Get original label values
industry_codes = encoders["Industry Code"].classes_
industry_names = encoders["Industry Name"].classes_
substance_names = encoders["Substance"].classes_
unit_names = encoders["Unit"].classes_

# Streamlit UI
st.title("🌍 Greenhouse Gas Emission Predictor")

st.markdown("Please select the inputs below to predict GHG Emission Factor:")

col1, col2 = st.columns(2)

with col1:
    selected_code = st.selectbox("Industry Code", industry_codes)
    selected_name = st.selectbox("Industry Name", industry_names)

with col2:
    selected_substance = st.selectbox("GHG Substance", substance_names)
    selected_unit = st.selectbox("Unit Type", unit_names)

margin_value = st.number_input("Margin of Supply Chain Emission Factor", min_value=0.0, step=0.001)

# Predict button
if st.button("🔮 Predict Emission Factor"):
    try:
        # Encode selected values
        code_enc = encoders["Industry Code"].transform([selected_code])[0]
        name_enc = encoders["Industry Name"].transform([selected_name])[0]
        sub_enc = encoders["Substance"].transform([selected_substance])[0]
        unit_enc = encoders["Unit"].transform([selected_unit])[0]

        # Prepare input and predict
        input_data = [[code_enc, name_enc, sub_enc, unit_enc, margin_value]]
        prediction = model.predict(input_data)[0]

        st.success(f"🌱 Predicted Supply Chain Emission Factor: **{prediction:.6f}**")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

