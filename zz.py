import streamlit as st
import joblib

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Manual mappings
industry_code_map = dict(enumerate(encoders["Industry Code"].classes_))
industry_name_map = dict(enumerate(encoders["Industry Name"].classes_))
substance_map = dict(enumerate(encoders["Substance"].classes_))
unit_map = dict(enumerate(encoders["Unit"].classes_))

# Real values for dropdowns
industry_codes = list(industry_code_map.values())
industry_names = list(industry_name_map.values())
substances = list(substance_map.values())
units = list(unit_map.values())

# UI
st.title("🌱 GHG Emission Factor Predictor")

industry_code = st.selectbox("Industry Code", industry_codes)
industry_name = st.selectbox("Industry Name", industry_names)
substance = st.selectbox("Substance", substances)
unit = st.selectbox("Unit", units)
margin = st.slider("Margin of Supply Chain Emission Factors", 0.0, 1.0, 0.05)

if st.button("🔮 Predict"):
    # Encode manually using reverse lookup
    code_encoded = list(industry_code_map.keys())[list(industry_code_map.values()).index(industry_code)]
    name_encoded = list(industry_name_map.keys())[list(industry_name_map.values()).index(industry_name)]
    sub_encoded = list(substance_map.keys())[list(substance_map.values()).index(substance)]
    unit_encoded = list(unit_map.keys())[list(unit_map.values()).index(unit)]

    X = [[code_encoded, name_encoded, sub_encoded, unit_encoded, margin]]
    prediction = model.predict(X)[0]

    st.success(f"🌍 Predicted Emission Factor: **{prediction:.4f}**")

    # Show real names (not numbers)
    st.markdown("### 📄 Prediction Input Summary")
    st.write(f"**Industry Code:** {industry_code}")
    st.write(f"**Industry Name:** {industry_name}")
    st.write(f"**Substance:** {substance}")
    st.write(f"**Unit:** {unit}")
    st.write(f"**Margin:** {margin}")



