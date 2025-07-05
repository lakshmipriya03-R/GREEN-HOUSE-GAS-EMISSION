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

    # Rename target column to simpler name
    df.rename(columns={
        'supply_chain_ghg_emission_factors_for_us_commodities_and_industries': 'emission_factor'
    }, inplace=True)

    # Drop rows with missing target values
    df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
    df = df.dropna(subset=['emission_factor'])

    # Clean 'name' column, remove empty strings
    df['name'] = df['name'].astype(str).str.strip()
    df = df[df['name'] != '']

    # Reset index after filtering
    df = df.reset_index(drop=True)

    return df

df = load_data()

X = df[['name']]
y = df['emission_factor']

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, ['name'])
    ])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

model.fit(X, y)

industry_input = st.selectbox("Select Industry Name", sorted(df['name'].unique()))

if st.button("Predict Emission Factor"):
    input_df = pd.DataFrame({'name': [industry_input]})
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Emission Factor: {pred:.4f}")










