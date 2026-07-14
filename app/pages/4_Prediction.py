import streamlit as st

st.set_page_config(page_title="Prediction", page_icon="🔮")

st.title("🔮 Customer Churn Prediction")

st.write("Fill in the customer details below.")

# -----------------------------
# Customer Information
# -----------------------------

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

if st.button("Predict Churn"):
    st.success("Prediction coming in the next step!")