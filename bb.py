import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

DATA_URL = "https://raw.githubusercontent.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/main/greenhouse_gas.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_URL)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

df = load_data()

required_cols = ['name', 'supply_chain_ghg_emission_factors_for_us_commodities_and_industries']
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset must contain columns: {required_cols}")
    st.stop()

# Prepare features and target
X = df[['name']]
y = pd.to_numeric(df['supply_chain_ghg_emission_factors_for_us_commodities_and_industries'], errors='coerce')
y = y.fillna(0)  # fill missing target values with 0, or choose appropriate strategy

categorical_features = ['name']
categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('cat', categorical_transformer, categorical_features)
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

model.fit(X, y)

industry_input = st.selectbox("Select Industry/Name", sorted(df['name'].unique()))

if st.button("Predict Emission Factor"):
    input_df = pd.DataFrame({'name': [industry_input]})
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Emission Factor: {pred:.4f}")





