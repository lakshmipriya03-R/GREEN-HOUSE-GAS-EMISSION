import streamlit as st
import joblib

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Get real (original) labels from encoders
industry_codes = list(encoders["Industry Code"].classes_)
industry_names = list(encoders["Industry Name"].classes_)
substances = list(encoders["Substance"].classes_)
units = list(encoders["Unit"].classes_)

# Title
st.title("🌱 GHG Emission Factor Predictor")

# Real-name inputs
selected_code = st.selectbox("Industry Code", industry_codes)
selected_name = st.selectbox("Industry Name", industry_names)
selected_substance = st.selectbox("Substance", substances)
selected_unit = st.selectbox("Unit", units)
margin = st.slider("Margin of Supply Chain Emission Factors", 0.0, 1.0, 0.05)

if st.button("🔮 Predict"):
    # Encode only for model input
    code_encoded = encoders["Industry Code"].transform([selected_code])[0]
    name_encoded = encoders["Industry Name"].transform([selected_name])[0]
    substance_encoded = encoders["Substance"].transform([selected_substance])[0]
    unit_encoded = encoders["Unit"].transform([selected_unit])[0]

    # Prediction input
    X = [[code_encoded, name_encoded, substance_encoded, unit_encoded, margin]]

    # Predict
    prediction = model.predict(X)[0]

    # Show real result
    st.success(f"🌍 Predicted Emission Factor: **{prediction:.4f}**")

    # Summary with real names
    st.markdown("### 📄 Input Summary")
    st.write(f"**Industry Code:** {selected_code}")
    st.write(f"**Industry Name:** {selected_name}")
    st.write(f"**Substance:** {selected_substance}")
    st.write(f"**Unit:** {selected_unit}")
    st.write(f"**Margin:** {margin}")



