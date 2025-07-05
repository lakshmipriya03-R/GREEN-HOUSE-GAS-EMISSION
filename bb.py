import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor

st.set_page_config(page_title="GHG Emission Predictor", layout="centered")
st.title("Greenhouse Gas Emission Predictor")

# Load from raw GitHub link
@st.cache_data
def load_data():
    url = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"
    df = pd.read_excel(url)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Normalize/rename for consistency
    df.rename(columns={
        "supply_chain_emission_factors_without_margins": "emission_factor"
    }, inplace=True)

    df["industry_name"] = df["industry_name"].astype(str).str.strip()
    df["substance"] = df["substance"].astype(str).str.strip()

    # Convert emission factor safely
    df["emission_factor"] = pd.to_numeric(df["emission_factor"], errors="coerce")

    # Drop rows with missing required values
    df.dropna(subset=["industry_name", "substance", "emission_factor"], inplace=True)

    return df

# Load dataset
df = load_data()

# Features and Target
X = df[["industry_name", "substance"]]
y = df["emission_factor"].astype(np.float32)

# Define pipeline
categorical_features = ["industry_name", "substance"]
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("cat", categorical_transformer, categorical_features)
])

model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", XGBRegressor(objective="reg:squarederror", n_estimators=100, random_state=42))
])

# Fit model
model_pipeline.fit(X, y)

# Streamlit UI
st.subheader("📊 Predict Emission Factor")

industry = st.selectbox("Select Industry", sorted(df["industry_name"].unique()))
substance = st.selectbox("Select Substance", sorted(df["substance"].unique()))

if st.button("Predict"):
    input_df = pd.DataFrame([[industry, substance]], columns=["industry_name", "substance"])
    prediction = model_pipeline.predict(input_df)[0]
    st.success(f"Predicted GHG Emission Factor: **{prediction:.6f}**")


