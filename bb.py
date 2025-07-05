import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

# Load data with robust error handling
@st.cache_data
def load_data():
    try:
        DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"
        df = pd.read_excel(DATA_URL)
        
        # Standardize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Identify target column (case-insensitive)
        target_cols = [col for col in df.columns if 'ghg' in col.lower() or 'emission' in col.lower()]
        if not target_cols:
            raise ValueError("No emission factor column found")
        
        # Clean and prepare data
        df = df.rename(columns={target_cols[0]: 'emission_factor'})
        df['name'] = df['name'].astype(str).str.strip()
        
        # Convert target to numeric, handling errors
        df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
        
        # Remove invalid rows
        df = df.dropna(subset=['emission_factor', 'name'])
        df = df[df['name'] != '']
        df = df[~df['emission_factor'].isin([np.inf, -np.inf])]
        
        if len(df) == 0:
            raise ValueError("No valid data remaining after cleaning")
            
        return df.reset_index(drop=True)
    
    except Exception as e:
        st.error(f"Data loading error: {str(e)}")
        return None

# Load and validate data
df = load_data()

if df is not None:
    try:
        # Prepare features and target
        X = df[['name']].copy()
        y = df['emission_factor'].values  # Convert to numpy array directly
        
        # Ensure data is properly formatted
        if not isinstance(y, np.ndarray):
            y = np.array(y, dtype=np.float32)
        
        # Build preprocessing pipeline
        categorical_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='constant', fill_value='unknown')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])

        preprocessor = ColumnTransformer([
            ('cat', categorical_transformer, ['name'])
        ])

        # Configure XGBoost with explicit parameters
        xgb_regressor = xgb.XGBRegressor(
            objective='reg:squarederror',
            random_state=42,
            enable_categorical=False,
            n_estimators=100,
            max_depth=3
        )

        # Create final pipeline
        model = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', xgb_regressor)
        ])

        # Train model with error handling
        model.fit(X, y)
        
        # Create prediction interface
        st.subheader("Make a Prediction")
        industry = st.selectbox(
            "Select Industry Name", 
            options=sorted(df['name'].unique()),
            index=0
        )
        
        if st.button("Predict Emission Factor"):
            try:
                input_data = pd.DataFrame({'name': [industry]})
                prediction = model.predict(input_data)[0]
                st.success(f"Predicted Emission Factor: {prediction:.4f}")
            except Exception as e:
                st.error(f"Prediction failed: {str(e)}")
                
    except Exception as e:
        st.error(f"Model training error: {str(e)}")

