# Telco Customer Churn Analysis - Final Report

## 1. Business Problem
26.5% of customers are churning annually. Acquiring a new customer costs 5x more than retaining an existing one. The objective is to predict high-risk customers early and reduce churn through targeted retention strategies.

## 2. Dataset Overview
- Source: Telco Customer Churn Dataset
- Size: 7,043 customers, 21 features
- Target: Churn (Yes/No) - Imbalanced, 26.5% Yes
- Features: Demographics, Services, Contract & Billing (tenure, MonthlyCharges, TotalCharges, Contract, InternetService, PaymentMethod)

## 3. Exploratory Data Analysis - Key Insights

**Contract Type is the strongest predictor:**
- Month-to-month: 42.7% churn rate
- One year: 11.3% churn rate
- Two year: 2.8% churn rate
- Customers without long-term commitment are 15x more likely to leave.

**Internet Service:**
- Fiber optic: 41.8% churn rate (highest)
- DSL: 19% churn rate
- No Internet Service: 7% churn rate
- Fiber optic users show dissatisfaction, likely due to price or speed issues.

**Payment Method:**
- Electronic check: 45% churn rate
- Bank transfer (automatic) / Credit card (automatic): ~15% churn rate

## 4. Model Performance
- Model: XGBoost Classifier
- Default threshold (0.5): Accuracy 75.7%, Recall for Churn 67%
- Optimized threshold (0.3 - Business focused): Accuracy 73%, Recall for Churn 80.4%
- Confusion Matrix at 0.3 threshold: [[733, 302], [73, 301]]
- Out of 374 actual churners in test set, model correctly identified 301.

## 5. Feature Importance
1. Contract_Two year (38%) - Strong protective factor
2. InternetService_Fiber optic (19%) - Major risk factor
3. Contract_One year (11%) - Protective factor
4. InternetService_No (5%)
5. PaymentMethod_Electronic check (3%)

## 6. Business Recommendations
1. Migrate Month-to-Month to Long-Term: Offer 20% discount or free upgrade to convert high-churn segment.
2. Audit Fiber Optic Service: Investigate speed, downtime, and pricing vs competitors.
3. Push Auto-Pay: Incentivize Electronic check users to move to automatic payments.
4. Proactive Retention: Flag customers with >30% churn probability and have retention team contact them.

## 7. Deployment
- API built with FastAPI (app.py)
- Artifacts: churn_model.pkl, model_columns.pkl
- Endpoint: POST /predict returns churn_chance_percent and risk label
- Docs: /docs

## 8. Next Steps
- Build dashboard for retention team
- Add SHAP explanations
- Retrain monthly
- A/B test retention offers
