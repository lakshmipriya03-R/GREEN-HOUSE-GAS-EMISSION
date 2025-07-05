import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"

@st.cache_data
def load_data():
    try:
        df = pd.read_excel(DATA_URL)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        if 'supply_chain_ghg_emission_factors_for_us_commodities_and_industries' in df.columns:
            df.rename(columns={'supply_chain_ghg_emission_factors_for_us_commodities_and_industries': 'emission_factor'}, inplace=True)

        df['name'] = df['name'].astype(str).str.strip()
        df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
        
        df = df.dropna(subset=['emission_factor'])
        df = df[df['name'] != '']
        df = df.reset_index(drop=True)
        
        if len(df) == 0:
            raise ValueError("No valid data remaining after preprocessing")
            
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

df = load_data()

if df is not None:
    try:
        X = df[['name']]
        y = df['emission_factor'].astype('float32')
        
        # Ensure we have valid data
        mask = ~y.isna() & ~y.isin([np.inf, -np.inf])
        y = y[mask]
        X = X.loc[mask]
        
        if len(X) == 0 or len(y) == 0:
            raise ValueError("No valid samples remaining after cleaning")
        
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
            try:
                input_df = pd.DataFrame({'name': [industry]})
                pred = model.predict(input_df)[0]
                st.success(f"Predicted Emission Factor: {pred:.6f}")
            except Exception as e:
                st.error(f"Prediction failed: {str(e)}")
                
    except Exception as e:
        st.error(f"Model training failed: {str(e)}")







