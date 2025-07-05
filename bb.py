import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt

st.title("Greenhouse Gas Emission Factor Model Training")

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.write("Dataset Preview:", df.head())

    # Check required columns
    required_cols = ['industry_name', 'substance', 'supply_chain_emission_factors_without_margins']
    if not all(col in df.columns for col in required_cols):
        st.error(f"Dataset must contain columns: {required_cols}")
        st.stop()

    X = df[['industry_name', 'substance']]
    y = df['supply_chain_emission_factors_without_margins']

    # Split dataset
    test_size = st.slider("Test set size (%)", 10, 50, 20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

    # Build pipeline
    categorical_features = ['industry_name', 'substance']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)
        ])

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', xgb.XGBRegressor(random_state=42, objective='reg:squarederror'))
    ])

    # Hyperparameter options
    n_iter = st.slider("Number of hyperparameter tuning iterations", 5, 50, 20)

    param_distributions = {
        'regressor__n_estimators': [100, 200, 300, 400],
        'regressor__max_depth': [3, 5, 7, 10],
        'regressor__learning_rate': [0.01, 0.05, 0.1, 0.2],
        'regressor__subsample': [0.6, 0.8, 1.0],
        'regressor__colsample_bytree': [0.6, 0.8, 1.0],
        'regressor__gamma': [0, 0.1, 0.3],
        'regressor__reg_alpha': [0, 0.1, 1],
        'regressor__reg_lambda': [1, 1.5, 2],
    }

    if st.button("Start Training"):
        with st.spinner("Training and tuning model, please wait..."):
            random_search = RandomizedSearchCV(
                model, param_distributions, n_iter=n_iter,
                scoring='r2', cv=5, verbose=1, random_state=42, n_jobs=-1
            )
            random_search.fit(X_train, y_train)

        st.success("Training complete!")

        best_model = random_search.best_estimator_
        y_pred = best_model.predict(X_test)

        st.write("### Evaluation Metrics on Test Set")
        st.write(f"R² Score: {r2_score(y_test, y_pred):.4f}")
        st.write(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")
        st.write(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")

        # Feature importance plot
        xgb_model = best_model.named_steps['regressor']
        onehot = best_model.named_steps['preprocessor'].transformers_[0][1].named_steps['onehot']
        feature_names = onehot.get_feature_names_out(categorical_features)

        importance = xgb_model.feature_importances_

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(feature_names, importance)
        ax.set_xlabel("Feature Importance")
        ax.set_title("XGBoost Feature Importance")
        st.pyplot(fig)
