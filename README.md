# Telco Customer Churn Prediction API

A production-ready FastAPI service that predicts whether a telco customer will churn. Built with XGBoost and deployed with FastAPI.

## Model Details
- Algorithm: XGBoost Classifier
- Threshold: 0.3 (If >= 30% → High Risk)
- Output: churn_chance_percent + risk label

## How to run it locally
1. pip install -r requirements.txt
2. uvicorn app:app --reload
3. Open in browser:
     - Swagger UI: http://127.0.0.1:8000/docs
     - Health Check: http://127.0.0.1:8000/

## API Usage
POST /predict
Request: tenure, MonthlyCharges, Contract etc.
Response: { "churn_chance_percent": 76.24, "prediction": "High Risk" }

## Tech Stack
Python, Pandas, XGBoost, FastAPI, Uvicorn
