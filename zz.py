import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("ghg_model.pkl")

# Hardcoded mappings (example — update to match your dataset)
industry_code_map = {
    0: "1111A0",
    1: "1111B0",
    2: "111200",
    3: "111300",
    4: "111400",
    5: "111900",
    6: "112120",
    7: "1121A0"
}

industry_name_map = {
    0: "Oilseed farming",
    1: "Grain farming",
    2: "Vegetable farming",
    3: "Fruit farming"
}

substance_map = {
    0: "carbon dioxide",
    1: "methane",
    2: "nitrous oxide",
    3: "other GHGs"
}

unit_map = {
    0: "kg/2018 USD, purchaser price",
    1: "kg CO2e/2018 USD, purchaser price"
}

# Streamlit UI
st.title("🌱 GHG Emission Factor Predictor")

# Dropdowns show readable names, but return index for prediction
industry_code = st.selectbox("Industry Code", list(industry_code_map.values()))
industry_name = st.selectbox("Industry Name", list(industry_name_map.values()))
substance = st.selectbox("Substance", list(substance_map.values()))
unit = st.selectbox("Unit", list(unit_map.values()))
margin = st.slider("Margin of Supply Chain Emission Factors", 0.0, 1.0, 0.01)

# Convert values back to encoded form for model
inv_industry_code = list(industry_code_map.keys())[list(industry_code_map.values()).index(industry_code)]
inv_industry_name = list(industry_name_map.keys())[list(industry_name_map.values()).index(industry_name)]
inv_substance = list(substance_map.keys())[list(substance_map.values()).index(substance)]
inv_unit = list(unit_map.keys())[list(unit_map.values()).index(unit)]

# Predict
if st.button("🔮 Predict Emission Factor"):
    X = np.array([[inv_industry_code, inv_industry_name, inv_substance, inv_unit, margin]])
    prediction = model.predict(X)[0]

    st.success(f"🌍 Predicted Emission Factor: **{prediction:.4f}**")
    st.markdown("### 📋 You selected:")
    st.write(f"**Industry Code:** {industry_code}")
    st.write(f"**Industry Name:** {industry_name}")
    st.write(f"**Substance:** {substance}")
    st.write(f"**Unit:** {unit}")
    st.write(f"**Margin:** {margin}")




