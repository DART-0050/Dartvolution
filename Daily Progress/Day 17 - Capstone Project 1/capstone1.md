# Capstone Project 1 : Student Score Prediction

## Goal

Predict a student's **math score** based on their background and other scores using ML.

---

## Tried

1. **Linear Regression**
   - R² Score: **0.88**
   - MSE: **29.09**
   - ✅ Best Performing Model

2. **Random Forest Regressor** (Tuned)
   - R² Score: 0.82
   - MSE: 43.38
   - Slightly overfit, less effective than LR for this linear dataset.

---

## 🧪 Preprocessing Pipeline

- `OneHotEncoder` for categorical features
- `StandardScaler` for numerical features
- Combined using `ColumnTransformer`
- Split: 80% train / 20% test

---

## 🛠 Hyperparameter Tuning

Used `RandomizedSearchCV` to tune Random Forest  
Best params: `n_estimators=100`, `max_depth=None`, etc.

---

## 📦 Model Export

Saved both models using `joblib`:

- `linear_regression_model.pkl`
- `random_forest_model.pkl`

Tested them on real custom input.

---

## 📌 Takeaway

> Simpler models like **Linear Regression** can outperform complex ones when the data relationships are **mostly linear**. Always test both!

---

## 🚀 Next Steps

- Try the same pipeline on other targets (e.g. `writing score`)
- Build a **Streamlit app** to make predictions interactively
- Try other regressors (like XGBoost or Ridge)
