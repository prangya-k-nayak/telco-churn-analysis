import streamlit as st

from src.ui.styles import apply_theme

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
)

apply_theme()

st.title("ℹ️ About This Project")

st.markdown("""
## 🎯 Project Overview

The **Telecom Customer Churn Dashboard** is an end-to-end Machine Learning application that helps analyze customer behavior and predict whether a telecom customer is likely to churn.

The project combines **data preprocessing, exploratory data analysis (EDA), machine learning, model evaluation, and an interactive Streamlit dashboard** into a single application.

---

## 🚀 Key Features

- 📊 Interactive Dataset Explorer
- 📈 Exploratory Data Analysis (EDA)
- 📉 Interactive Plotly Visualizations
- 🤖 Machine Learning Model Comparison
- 🔮 Real-time Customer Churn Prediction
- 📊 Prediction Probability Score
- 💡 Business Recommendations
- 🌐 Multi-page Streamlit Dashboard

---

## 🛠️ Technology Stack

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Plotly
- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Deployment

- Streamlit

---

## 🤖 Machine Learning Models

- Logistic Regression
- Random Forest Classifier

### Best Model Performance

| Model | Accuracy |
|-------|---------:|
| Logistic Regression | **81.55%** |
| Random Forest | **79.63%** |

---

## 📊 Dataset

**IBM Telco Customer Churn Dataset**

Dataset Summary:

- 7,043 Customer Records
- 21 Features
- Binary Classification Problem
- Target Variable: **Churn (Yes / No)**

---

## 📈 Dashboard Modules

🏠 Home

- Project Overview
- Customer Statistics

📊 Dataset

- Dataset Preview
- Missing Values
- Column Information
- Dataset Download

📈 Exploratory Data Analysis

- Customer Demographics
- Service Analysis
- Billing Analysis
- Correlation Heatmap
- Business Insights

🤖 Model Performance

- Model Comparison
- Classification Report
- Confusion Matrix

🔮 Prediction

- Customer Profile Input
- Churn Prediction
- Prediction Probability
- Business Recommendation

---

## 🎯 Business Objective

This project enables telecom companies to:

- Identify customers who are likely to churn.
- Understand important churn patterns.
- Support customer retention strategies.
- Assist business decision-making using Machine Learning.

---

## 👩‍💻 Developed By

**Prangya Kumari Nayak**

MCA (Artificial Intelligence & Machine Learning)

Jain (Deemed-to-be University)

---

## 🔗 Project Links

**GitHub Repository**

https://github.com/prangya-k-nayak/telco-churn-analysis

**Live Streamlit App**

https://telco-churn-analysis-c66ns8v7eks7cpn3ewwwu7.streamlit.app

---

### ⭐ Thank you for exploring this project!

This dashboard demonstrates an end-to-end Machine Learning workflow, from data analysis and visualization to model development, evaluation, deployment, and interactive prediction.
""")