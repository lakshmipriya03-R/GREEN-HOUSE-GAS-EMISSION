import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import numpy as np

st.title("Greenhouse Gas Emission Predictor")

DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_URL)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Rename column if needed
    if 'supply_chain_ghg_emission_factors_for_us_commodities_and_industries' in df.columns:
        df.rename(columns={
            'supply_chain_ghg_emission_factors_for_us_commodities_and_industries': 'emission_factor'
        }, inplace=True)

    df = df.rename(columns={'name': 'industry_name'})  # Make sure this is consistent

    df['industry_name'] = df['industry_name'].astype(str).str.strip()
    df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')

    # Drop rows with missing values
    df = df.dropna(subset=['emission_factor', 'industry_name'])
    df = df[df['industry_name'] != '']
    df = df.reset_index(drop=True)
    return df

df = load_data()

X = df[['industry_name']]
y = df['emission_factor'].astype(np.float32)

# Preprocessing pipeline
cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('cat', cat_pipe, ['industry_name'])
])

# Full model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

# Fit model
model.fit(X, y)

# Streamlit UI
st.subheader("Predict GHG Emission Factor")
industry = st.selectbox("Select Industry Name", options=sorted(df['industry_name'].unique()))

if st.button("Predict"):
    input_df = pd.DataFrame({'industry_name': [industry]})
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Emission Factor: {prediction:.6f}")

