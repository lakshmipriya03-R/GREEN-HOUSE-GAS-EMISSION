import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def load_data(path_or_url):
    df = pd.read_excel(path_or_url)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    if 'supply_chain_ghg_emission_factors_for_us_commodities_and_industries' in df.columns:
        df.rename(columns={
            'supply_chain_ghg_emission_factors_for_us_commodities_and_industries': 'emission_factor'
        }, inplace=True)
        
    df['name'] = df['name'].astype(str).str.strip()
    df['emission_factor'] = pd.to_numeric(df['emission_factor'], errors='coerce')
    df = df.dropna(subset=['emission_factor'])
    df = df[df['name'] != '']
    df = df.reset_index(drop=True)
    return df

def train_and_evaluate(df):
    X = df[['name']]
    y = df['emission_factor'].astype('float32')

    # Pipeline for categorical encoding
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

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print("R² Score:", r2_score(y_test, preds))
    print("MAE:", mean_absolute_error(y_test, preds))
    print("MSE:", mean_squared_error(y_test, preds))
    
    return model

if __name__ == "__main__":
    DATA_URL = "https://github.com/lakshmipriya03-R/GREEN-HOUSE-GAS-EMISSION/raw/main/greenhouse_gas.xlsx"
    df = load_data(DATA_URL)
    trained_model = train_and_evaluate(df)
    # Optionally, save your model here with joblib or pickle if needed
