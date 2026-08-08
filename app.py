from fastapi import FastAPI
import os
import pandas as pd
import joblib
import traceback
from pathlib import Path

app = FastAPI(
    title= "Telco Churn Prediction API",
    description= "Predicts churn chance for new customers",
    version = "1.0"
)

# Load model and import columns
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "churn_model.pkl"
COLUMNS_PATH = BASE_DIR / "model_columns.pkl"

model = None
model_columns = None

@app.on_event('startup')
def load_artifacts():
    global model, model_columns
    print(f'Looking for model at: {MODEL_PATH}')
    print(f'Looking for columns at: {COLUMNS_PATH}')
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        print('Model Loaded!')
    else:
        print('Model file NOT FOUND!')
    if COLUMNS_PATH.exists():
        model_columns = joblib.load(COLUMNS_PATH)
        print(f'Columns Loaded: {len(model_columns)} cols')
    else:
        print('Columns file NOT FOUND!')

@app.get("/")
def home():
    return {
        "status":"API is running",
        "model_loaded": model is not None,
        "columns_loaded": model_columns is not None,
        "how_to_use": "Go to /docs for Swagger UI"
    }

@app.post("/predict")
def predict(data: dict):
    """
    Pass raw customer data as JSON. Example:
    {
      "tenure": 2,
      "MonthlyCharges": 95.5,
      "TotalCharges": 190,
      "Contract": "Month-to-month",
      "InternetService": "Fiber optic",
      "PaymentMethod": "Electronic check",
      "gender": "Male",
      "SeniorCitizen": 0,
      "Partner": "No",
      ...
    }
    """
    try:
        if model is None:
            return {"error": "Model not loaded. Check churn_model.pkl exists in same folder as app.py"}
        if model_columns is None:
            return {'error':'Modelcolumns.pkl not loaded. Save X.columns.tolist() as model_columns.pkl'}

        df_raw = pd.DataFrame([data])
        df_encoded = pd.get_dummies(df_raw)
        df_final = df_encoded.reindex(columns=model_columns, fill_value=0)

        if df_final.shape[1] != len(model_columns):
            return {'error': f'feature mismatch: got {df_final.shape[1]} expected {len(model_columns)}'}

        proba = model.predict_proba(df_final)[:,1][0]
        return {
            'churn_chance_percent': round(float(proba*100), 2),
            'prediction':"High Risk - Retention Needed" if proba >=0.3 else "Row Risk",
            'threshold_used':0.3
        }
    except Exception as e:
        return {
            'error': str(e),
            'trace':traceback.format_exc(),
            'received_data': data
        }
