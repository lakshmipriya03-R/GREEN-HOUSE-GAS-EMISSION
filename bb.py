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

    # Rename target column for convenience
    df.rename(columns={
        'supply_chain_ghg_emission_factors_for_us_commodities_and_industries': 'emission_factor'
    }, inplace=True)

    # Keep only rows with required columns and non-null targets
    df = df[['name', 'emission_factor']].copy()
    df['name'] = df['name'].astype(str).str.strip()
    df = df[df['name'] != '']
    df = df.dropna(subset=['emission_factor']).reset_index(drop=True)

    return df

df = load_data()

required_cols = ['name', 'emission_factor']
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset must contain columns: {required_cols}")
    st.stop()

X = df[['name']]  # must be DataFrame, not Series
y = df['emission_factor']

# Pipeline for categorical column 'name'
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
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Emission Factor: {prediction:.4f}")









