import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

DATA_FILE = "greenhouse_data.xlsx"  # Make sure this file is in the same folder as bb.py

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_FILE)
    return df

df = load_data()

required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset missing required columns: {required_cols}")
    st.stop()

st.write("Dataset preview:")
st.dataframe(df.head())

# Prepare features and target
X = df[['industry_name', 'substance']]
y = df['supply_chain_emission_factors_without_margins']

# Preprocessing pipeline for categorical features
categorical_features = ['industry_name', 'substance']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical_features)
])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

# Train model on full dataset (no test split for now)
model.fit(X, y)

# User input widgets
industry_input = st.selectbox("Select Industry", options=sorted(df['industry_name'].unique()))
substance_input = st.selectbox("Select Substance", options=sorted(df['substance'].unique()))

if st.button("Predict Emission Factor"):
    input_df = pd.DataFrame({'industry_name': [industry_input], 'substance': [substance_input]})
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Supply Chain Emission Factor: {prediction:.4f}")



