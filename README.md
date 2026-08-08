# Telco Customer Churn Prediction API

A production-ready FastAPI service that predicts whether a telco customer will churn. Built with XGBoost and deployed with FastAPI.

## 🚀 Live Demo
- Swagger UI: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/

## 🧠 Model Details
- Algorithm: XGBoost Classifier
- Threshold: 0.3 (If >= 30% → High Risk)
- Output: churn_chance_percent + risk label

## ⚙️ Installation & Run
pip install -r requirements.txt
uvicorn app:app --reload

## 📬 API Usage
POST /predict
Request: tenure, MonthlyCharges, Contract etc.
Response: { "churn_chance_percent": 76.24, "prediction": "High Risk" }

## 🛠️ Tech Stack
Python, Pandas, XGBoost, FastAPI, Uvicorn