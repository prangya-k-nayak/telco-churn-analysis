import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import joblib

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.models.load_model import load_model

st.set_page_config(page_title="Prediction", page_icon="🔮")

st.title("🔮 Customer Churn Prediction")

# ---------------- Load Model ---------------- #

model = load_model("logistic_regression.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/label_encoders.pkl")

# ---------------- User Inputs ---------------- #

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure", 0, 72, 12)

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

if st.button("Predict Churn"):

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
        st.error("🔴 Customer is likely to Churn")
    else:
        st.success("🟢 Customer is likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

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