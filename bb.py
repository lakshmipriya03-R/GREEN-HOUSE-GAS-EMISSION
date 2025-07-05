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

        # Handle target column naming
        target_col = [col for col in df.columns if 'ghg' in col.lower() or 'emission' in col.lower()]
        if target_col:
            df = df.rename(columns={target_col[0]: 'emission_factor'})
        else:
            raise ValueError("Could not find emission factor column")

        # Clean data
        df['name'] = df['name'].astype(str).str.strip()
        df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
        
        # Remove invalid rows
        df = df.dropna(subset=['emission_factor', 'name'])
        df = df[df['name'] != '']
        df = df[~df['emission_factor'].isin([np.inf, -np.inf])]
        
        if len(df) == 0:
            raise ValueError("No valid data remaining after cleaning")
            
        return df.reset_index(drop=True)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

df = load_data()

if df is not None:
    try:
        X = df[['name']]
        y = df['emission_factor'].astype('float32')
        
        # Final validation
        if len(X) != len(y):
            raise ValueError("Feature and target lengths don't match")
        if len(X) == 0:
            raise ValueError("No valid samples available for training")

        # Build pipeline
        cat_pipe = Pipeline([
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])

        preprocessor = ColumnTransformer([
            ('cat', cat_pipe, ['name'])
        ])

        model = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', xgb.XGBRegressor(
                objective='reg:squarederror',
                random_state=42,
                enable_categorical=False
            ))
        ])

        # Train model
        model.fit(X, y)

        # Prediction interface
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







