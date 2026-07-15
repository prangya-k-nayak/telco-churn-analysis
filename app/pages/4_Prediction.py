import sys
from pathlib import Path
import pandas as pd
import joblib

project_root = Path(__file__).resolve().parent.parent.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from src.ui.styles import apply_theme
from src.models.load_model import load_model

st.set_page_config(page_title="Prediction", page_icon="🔮")

apply_theme()

st.title("🔮 Customer Churn Prediction")

# ---------------- Load Model ---------------- #

model = load_model("logistic_regression.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/label_encoders.pkl")

# ---------------- User Inputs ---------------- #
st.markdown("## 👤 Customer Profile")

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 72, 12)

st.divider()

st.markdown("## 📡 Services")

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"],
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"],
)

security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"],
)

backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"],
)

device = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"],
)

support = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"],
)

tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"],
)

movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"],
)

st.divider()

st.markdown("## 💳 Billing")

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"],
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"],
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)",
    ],
)

st.divider()

st.markdown("## 💰 Charges")

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0,
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0,
)

# ---------------- Prediction ---------------- #

predict = st.button(
    "🚀 Predict Customer Churn",
    width="stretch",
)

if predict:

    data = pd.DataFrame(
        {
            "gender": [gender],
            "SeniorCitizen": [senior],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone],
            "MultipleLines": [multiple],
            "InternetService": [internet],
            "OnlineSecurity": [security],
            "OnlineBackup": [backup],
            "DeviceProtection": [device],
            "TechSupport": [support],
            "StreamingTV": [tv],
            "StreamingMovies": [movies],
            "Contract": [contract],
            "PaperlessBilling": [paperless],
            "PaymentMethod": [payment],
            "MonthlyCharges": [monthly],
            "TotalCharges": [total],
        }
    )

    for col in encoders:
        if col in data.columns:
            data[col] = encoders[col].transform(data[col])

    data = scaler.transform(data)

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error("🔴 High Risk: This customer is likely to churn.")
    else:
        st.success("🟢 Low Risk: This customer is likely to stay.")
    
    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    if probability > 0.7:
        st.warning(
            "Recommendation: Offer discounts or a long-term contract."
        )
    elif probability > 0.4:
        st.info(
            "Recommendation: Monitor customer satisfaction."
        )
    else:
        st.success(
            "Recommendation: Customer appears loyal."
        )

    st.divider()

    st.subheader("📋 Prediction Summary")

    summary = pd.DataFrame(
        {
            "Attribute": [
                "Contract",
                "Internet",
                "Monthly Charges",
                "Tenure",
                "Prediction",
            ],
            "Value": [
                contract,
                internet,
                f"${monthly:.2f}",
                tenure,
                "Churn" if prediction == 1 else "Stay",
            ],
        }
    )

    st.dataframe(summary, width="stretch")

    st.caption(
        "This prediction is generated using a machine learning model trained on the IBM Telco Customer Churn dataset. It is intended for demonstration purposes and should support—not replace—business decision-making."
    )