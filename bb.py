import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_URL)
    # Clean columns
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    # Rename target col for ease
    if 'supply_chain_ghg_emission_factors_for_us_commodities_and_industries' in df.columns:
        df = df.rename(columns={'supply_chain_ghg_emission_factors_for_us_commodities_and_industries':'emission_factor'})
    # Keep required cols only
    df = df[['name', 'emission_factor']].copy()
    # Clean data
    df['name'] = df['name'].astype(str).str.strip()
    df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
    df = df.dropna(subset=['emission_factor'])
    df = df[df['name'] != '']
    df = df.reset_index(drop=True)
    return df

df = load_data()

X = df[['name']]
y = df['emission_factor']

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('cat', cat_pipe, ['name'])
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

model.fit(X, y)

industry = st.selectbox("Select Industry Name", options=sorted(df['name'].unique()))

if st.button("Predict Emission Factor"):
    pred = model.predict(pd.DataFrame({'name':[industry]}))[0]
    st.success(f"Predicted Emission Factor: {pred:.6f}")












