# Telco Customer Churn - Final Report

## 1. Business Problem
Company ke 26% customers har saal chale ja rahe hain. Har customer ko rokne se company ko $$$ bachte hain.

## 2. Data
7043 customers, 21 columns. Target = Churn (Yes/No)

## 3. Key Insights (EDA se)
- Two year contract walo ka churn sirf 2.8% vs Month-to-month walo ka 42%
- Fiber optic walo ka churn 41.8% vs DSL walo ka 14%
- Electronic check se pay karne wale sabse zyada ja rahe hain

## 4. Model Performance
- Model: XGBoost
- Accuracy: 75.7% (0.5 threshold), 73% (0.3 threshold)
- Recall for Churn: 67% se badh ke 80% (0.3 threshold pe)
- Confusion Matrix (0.3 threshold): [[733 302] [73 301]]
- Matlab 374 mein se 301 churners ko pehle hi pakad liya

## 5. Top Reasons (Feature Importance)
1. Contract_Two year (38%) - Hero
2. Fiber optic (19%) - Villain
3. Contract_One year (11%) - Hero
4. No Internet (5%)
5. StreamingMovies (3%)

## 6. Business Recommendations
1. Month-to-month walo ko 1-year / 2-year pe lao - 20% discount do
2. Fiber optic service ka audit karo - speed / price ka issue hai
3. Electronic check walo ko auto-pay pe shift karo
4. 30% se zyada risk wale customers ko retention team call kare

## 7. Next Steps
- FastAPI se API banao (app.py ready hai)
- Dashboard banao
- Har mahine model ko naye data se retrain karo
