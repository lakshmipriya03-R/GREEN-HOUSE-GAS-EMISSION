import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb
from sklearn.model_selection import train_test_split

st.title("Greenhouse Gas Emission Predictor")

@st.cache_data
def load_and_preprocess_data():
    try:
        # Load data
        DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"
        df = pd.read_excel(DATA_URL)
        
        # Standardize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Identify target column
        target_col = next((col for col in df.columns if 'ghg' in col.lower() or 'emission' in col.lower()), None)
        if not target_col:
            raise ValueError("Could not identify emission factor column")
        
        # Clean and prepare data
        df = df.rename(columns={target_col: 'emission_factor'})
        df['name'] = df['name'].astype(str).str.strip()
        
        # Convert target to numeric with strict validation
        df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
        
        # Remove invalid data points
        df = df.dropna(subset=['emission_factor', 'name'])
        df = df[df['name'] != '']
        df = df[~df['emission_factor'].isin([np.inf, -np.inf])]
        
        if len(df) < 10:  # Minimum threshold for meaningful modeling
            raise ValueError("Insufficient valid data points after cleaning")
            
        return df
    
    except Exception as e:
        st.error(f"Data loading error: {str(e)}")
        st.stop()
        return None

# Load and validate data
df = load_and_preprocess_data()

# Prepare features and target with explicit type conversion
X = df[['name']].copy()
y = df['emission_factor'].values.astype(np.float32)  # Explicit float32 conversion

# Verify data shapes and types
if len(X) != len(y):
    st.error("Feature and target dimensions don't match")
    st.stop()

# Build robust modeling pipeline
try:
    # Preprocessing for categorical features
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer([
        ('cat', categorical_transformer, ['name'])
    ])

    # Configure XGBoost with conservative settings
    xgb_model = xgb.XGBRegressor(
        objective='reg:squarederror',
        random_state=42,
        n_estimators=150,
        max_depth=5,
        learning_rate=0.1,
        enable_categorical=False,
        verbosity=1
    )

    # Create final pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', xgb_model)
    ])

    # Train with validation split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    
    # Simple validation check
    train_score = model.score(X_train, y_train)
    val_score = model.score(X_val, y_val)
    st.write(f"Model trained successfully (Train R²: {train_score:.2f}, Val R²: {val_score:.2f})")

    # Prediction interface
    st.subheader("Make a Prediction")
    industry = st.selectbox(
        "Select Industry Name", 
        options=sorted(df['name'].unique()),
        index=0
    )
    
    if st.button("Predict Emission Factor"):
        try:
            input_df = pd.DataFrame({'name': [industry]})
            prediction = model.predict(input_df)[0]
            st.success(f"Predicted Emission Factor: {prediction:.4f}")
            st.write(f"Industry: {industry}")
        except Exception as e:
            st.error(f"Prediction failed: {str(e)})
            
except Exception as e:
    st.error(f"Model training error: {str(e)}")
    st.stop()

