import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import xgboost as xgb
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

st.title("Greenhouse Gas Emission Factor Model Training")

# Load dataset (make sure the file is in the same folder as bb.py)
DATA_FILE = "greenhouse_data.xlsx"  # <-- Update with your actual filename

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_FILE)
    return df

df = load_data()

required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']
if not all(col in df.columns for col in required_cols):
    st.error(f"Dataset missing required columns: {required_cols}")
    st.stop()

st.success("Dataset loaded successfully!")
st.write(df.head())

# Prepare features and target
X = df[['industry_name', 'substance']]
y = df['supply_chain_emission_factors_without_margins']

# Split data
test_size = st.slider("Test set size (%)", 10, 50, 20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

# Preprocessing pipeline for categorical features
categorical_features = ['industry_name', 'substance']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer(transformers=[
    ('cat', categorical_transformer, categorical_features)
])

# Model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(objective='reg:squarederror', random_state=42))
])

# Train model button
if st.button("Train Model"):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.write("### Model Evaluation on Test Set")
    st.write(f"R² Score: {r2_score(y_test, y_pred):.4f}")
    st.write(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")
    st.write(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")

    # Show some predictions vs actuals
    result_df = X_test.copy()
    result_df['Actual'] = y_test
    result_df['Predicted'] = y_pred
    st.write(result_df.head(10))

