import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("ghg_model.pkl")
encoders = joblib.load("ghg_encoders.pkl")

# Load original label names
industry_code_labels = encoders["Industry Code"].classes_.tolist()
industry_name_labels = encoders["Industry Name"].classes_.tolist()
substance_labels = encoders["Substance"].classes_.tolist()
unit_labels = encoders["Unit"].classes_.tolist()

# Streamlit UI
st.title("🌍 Greenhouse Gas Emission Predictor")
st.markdown("Select industry details to predict GHG Emission Factor:")

col1, col2 = st.columns(2)

with col1:
    industry_code = st.selectbox("📦 Industry Code", industry_code_labels)
    industry_name = st.selectbox("🏭 Industry Name", industry_name_labels)

with col2:
    substance = st.selectbox("🧪 GHG Substance", substance_labels)
    unit = st.selectbox("⚖️ Unit", unit_labels)

margin = st.number_input("📈 Margin of Supply Chain Emission Factor", min_value=0.0, step=0.001)

# Predict
if st.button("🔮 Predict Emission Factor"):
    try:
        # Encode inputs
        code_encoded = encoders["Industry Code"].transform([industry_code])[0]
        name_encoded = encoders["Industry Name"].transform([industry_name])[0]
        sub_encoded = encoders["Substance"].transform([substance])[0]
        unit_encoded = encoders["Unit"].transform([unit])[0]

        # Prepare input and predict
        input_data = [[code_encoded, name_encoded, sub_encoded, unit_encoded, margin]]
        prediction = model.predict(input_data)[0]

        # Show result with real values
        st.success(f"""
        ✅ **Predicted Emission Factor**: `{prediction:.6f}`

        📦 **Industry Code**: {industry_code}  
        🏭 **Industry Name**: {industry_name}  
        🧪 **Substance**: {substance}  
        ⚖️ **Unit**: {unit}  
        📈 **Margin**: {margin}
        """)
    except Exception as e:
        st.error(f"Error: {e}")

