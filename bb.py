import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

# Load dataset
DATA_FILE = "greenhouse_data.xlsx"
df = pd.read_excel(DATA_FILE)

# Required columns
required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset missing required columns: {required_cols}")
    st.stop()

# Prepare training data
X = df[['industry_name', 'substance']]
y = df['supply_chain_emission_factors_without_margins']

# Preprocessing
categorical_features = ['industry_name', 'substance']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical_features)
])

# Model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

# Train model on all data (since no train/test split here)
model.fit(X, y)

# User input
industry_input = st.selectbox("Select Industry", options=sorted(df['industry_name'].unique()))
substance_input = st.selectbox("Select Substance", options=sorted(df['substance'].unique()))

# Predict button
if st.button("Predict Emission Factor"):
    input_df = pd.DataFrame({'industry_name': [industry_input], 'substance': [substance_input]})
    pred = model.predict(input_df)[0]
    st.write(f"Predicted Supply Chain Emission Factor: **{pred:.4f}**")


