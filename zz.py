import streamlit as st
import pandas as pd
import joblib

# Load saved model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Create dropdowns with original (real) values
industry_codes = list(encoders["Industry Code"].classes_)
industry_names = list(encoders["Industry Name"].classes_)
substances = list(encoders["Substance"].classes_)
units = list(encoders["Unit"].classes_)

# --- UI ---
st.title("🌍 GHG Emission Factor Predictor")

industry_code = st.selectbox("Industry Code", industry_codes)
industry_name = st.selectbox("Industry Name", industry_names)
substance = st.selectbox("Substance", substances)
unit = st.selectbox("Unit", units)
margin = st.slider("Margin of Supply Chain Emission Factors", 0.0, 1.0, 0.05)

# --- Predict ---
if st.button("🔮 Predict Emission Factor"):
    try:
        # Encode inputs
        ic = encoders["Industry Code"].transform([industry_code])[0]
        iname = encoders["Industry Name"].transform([industry_name])[0]
        sub = encoders["Substance"].transform([substance])[0]
        uni = encoders["Unit"].transform([unit])[0]

        # Predict
        X = [[ic, iname, sub, uni, margin]]
        prediction = model.predict(X)[0]

        # Show result
        st.success(f"✅ Predicted Emission Factor: **{prediction:.4f}**")
        st.markdown("---")
        st.markdown("### 🔍 Input Summary")
        st.write(f"**Industry Code:** {industry_code}")
        st.write(f"**Industry Name:** {industry_name}")
        st.write(f"**Substance:** {substance}")
        st.write(f"**Unit:** {unit}")
        st.write(f"**Margin:** {margin}")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")



