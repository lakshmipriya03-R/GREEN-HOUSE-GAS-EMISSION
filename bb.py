import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb

st.title("Greenhouse Gas Emission Predictor")

uploaded_file = st.file_uploader("Upload your dataset (Excel or CSV)", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']
    if not all(col in df.columns for col in required_cols):
        st.error(f"Dataset must contain columns: {required_cols}")
        st.stop()

    st.write("Dataset preview:")
    st.dataframe(df.head())

    X = df[['industry_name', 'substance']]
    y = df['supply_chain_emission_factors_without_margins']

    categorical_features = ['industry_name', 'substance']
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

    industry_input = st.selectbox("Select Industry", sorted(df['industry_name'].unique()))
    substance_input = st.selectbox("Select Substance", sorted(df['substance'].unique()))

    if st.button("Predict Emission Factor"):
        input_df = pd.DataFrame({'industry_name': [industry_input], 'substance': [substance_input]})
        pred = model.predict(input_df)[0]
        st.success(f"Predicted Supply Chain Emission Factor: {pred:.4f}")

else:
    st.info("Please upload your dataset file to start.")




