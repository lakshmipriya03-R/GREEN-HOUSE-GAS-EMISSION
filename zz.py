import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

st.set_page_config(page_title="GHG Emission Predictor", layout="centered")
st.title("🌍 GHG Emission Factor Predictor")
st.markdown("Enter industry details to predict the **Supply Chain Emission Factor (without margins)**.")

# Sample values from training (you can make dynamic with real df if needed)
industry_codes = encoders["Industry Code"].classes_.tolist()
industry_names = encoders["Industry Name"].classes_.tolist()
substances = encoders["Substance"].classes_.tolist()
units = encoders["Unit"].classes_.tolist()

# --- Input Fields ---
industry_code = st.selectbox("🔢 Industry Code", industry_codes)
industry_name = st.selectbox("🏭 Industry Name", industry_names)
substance = st.selectbox("🧪 Substance", substances)
unit = st.selectbox("📏 Unit", units)
margin = st.number_input("📉 Margin of Supply Chain Emission Factor", min_value=0.0, step=0.001)

# --- Predict ---
if st.button("🔍 Predict Emission Factor"):
    # Encode inputs
    ic = encoders["Industry Code"].transform([industry_code])[0]
    iname = encoders["Industry Name"].transform([industry_name])[0]
    sub = encoders["Substance"].transform([substance])[0]
    un = encoders["Unit"].transform([unit])[0]

    # Create input DataFrame
    input_df = pd.DataFrame([[ic, iname, sub, un, margin]],
                            columns=["Industry Code", "Industry Name", "Substance", "Unit", "Margins of Supply Chain Emission Factors"])

    # Predict
    prediction = model.predict(input_df)[0]

    st.success(f"💡 **Predicted Emission Factor (no margins):** `{prediction:.6f}` kg CO₂e/2018 USD")
