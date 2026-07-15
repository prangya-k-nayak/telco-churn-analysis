import sys
from pathlib import Path
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder

project_root = Path(__file__).resolve().parent.parent.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from src.ui.styles import apply_theme
from src.data.loader import load_telco_churn_data

st.set_page_config(page_title="EDA", page_icon="📈")

apply_theme()

df = load_telco_churn_data()

st.title("📈 Exploratory Data Analysis")

st.markdown("""
Explore customer behaviour, service usage, billing patterns and their
relationship with customer churn through interactive visualizations.
""")

st.divider()

st.header("👥 Customer Demographics")

# -----------------------------
# Churn Distribution
# -----------------------------
st.subheader("Customer Churn Distribution")

fig = px.pie(
    df,
    names="Churn",
    hole=0.65,
    color="Churn",
    title="Customer Churn Distribution",
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(fig, width="stretch")

st.info(
    "📌 Around 26% of customers have churned while nearly 74% remain active."
)

st.subheader("Gender vs Churn")

fig = px.bar(
    df,
    x="gender",
    color="Churn",
    barmode="group",
)

st.plotly_chart(fig, width="stretch")

st.info(
    "📌 Compare churn counts across male and female customers."
)

st.subheader("Senior Citizen vs Churn")

fig = px.histogram(
    df,
    x="SeniorCitizen",
    color="Churn",
    barnorm="percent",
)

st.plotly_chart(fig, width="stretch")

st.info(
    "📌 Shows the percentage of customers who churned within each age group."
)

st.divider()

st.header("📡 Service Analysis")

# -----------------------------
# Internet Service vs Churn
# -----------------------------
st.subheader("Internet Service vs Churn")

fig = px.bar(
    df,
    x="InternetService",
    color="Churn",
    barmode="group",
)

st.plotly_chart(fig, width="stretch")

st.info(
    "📌 Compare churn across DSL, Fiber Optic, and customers without internet service."
)

# -----------------------------
# Online Security vs Churn
# -----------------------------
st.subheader("Online Security vs Churn")

fig = px.bar(
    df,
    y="OnlineSecurity",
    color="Churn",
    orientation="h",
)

st.plotly_chart(fig, width="stretch")

st.info(
    "📌 Customers without online security generally exhibit higher churn."
)

st.divider()

st.header("💳 Billing & Contract")

# -----------------------------
# Contract vs Churn
# -----------------------------
st.subheader("Contract Type vs Churn")

fig = px.bar(
    df,
    y="Contract",
    color="Churn",
    orientation="h",
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Customers with month-to-month contracts tend to churn more frequently than customers with long-term contracts."
)

# -----------------------------
# Payment Method vs Churn
# -----------------------------
st.subheader("Payment Method vs Churn")

fig = px.bar(
    df,
    y="PaymentMethod",
    color="Churn",
    orientation="h",
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Different payment methods show varying churn behaviour among customers."
)

# -----------------------------
# Paperless Billing vs Churn
# -----------------------------
st.subheader("Paperless Billing vs Churn")

fig = px.histogram(
    df,
    x="PaperlessBilling",
    color="Churn",
    barnorm="percent",
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Compare churn percentages between customers using paperless and traditional billing."
)

st.divider()

st.header("📈 Numerical Feature Analysis")

# -----------------------------
# Tenure Distribution
# -----------------------------
st.subheader("Customer Tenure Distribution")

fig = px.histogram(
    df,
    x="tenure",
    nbins=30,
    color_discrete_sequence=["#8B5CF6"],
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Shows how long customers have stayed with the company."
)

# -----------------------------
# Monthly Charges Distribution
# -----------------------------
st.subheader("Monthly Charges Distribution")

fig = px.histogram(
    df,
    x="MonthlyCharges",
    nbins=30,
    color_discrete_sequence=["#2DD4BF"],
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Displays the distribution of monthly subscription charges."
)

st.subheader("Monthly Charges vs Churn")

fig = px.box(
    df,
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    points="outliers",
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Compare the distribution of monthly charges for customers who stayed versus those who churned."
)

# ==========================================================
# Correlation Analysis
# ==========================================================

st.divider()

st.header("📊 Correlation Analysis")

st.markdown(
    "Explore the relationships between the encoded features."
)

# Create a copy so the original dataframe is not modified
corr_df = df.copy()

encoder = LabelEncoder()

for column in corr_df.columns:
    if corr_df[column].dtype == "object":
        corr_df[column] = encoder.fit_transform(
            corr_df[column].astype(str)
        )

correlation = corr_df.corr(numeric_only=True)

fig = go.Figure(
    data=go.Heatmap(
        z=correlation.values,
        x=correlation.columns,
        y=correlation.columns,
        colorscale="RdBu",
        zmid=0,
        text=correlation.round(2).values,
        texttemplate="%{text}",
        hoverongaps=False,
    )
)

fig.update_layout(
    title="Feature Correlation Heatmap",
    height=750,
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "The heatmap highlights positive and negative relationships among encoded variables."
)

# ==========================================================
# Business Insights
# ==========================================================

st.divider()

st.header("💡 Key Business Insights")

st.success("""
### Important Findings

✅ Customers with **Month-to-Month contracts** show the highest churn.

✅ Customers **without Online Security** are more likely to leave.

✅ Customers **without Tech Support** tend to churn more frequently.

✅ Customers with **longer tenure** are generally more loyal.

✅ Higher **Monthly Charges** are associated with increased churn risk.

✅ **Fiber Optic Internet** customers exhibit relatively higher churn than DSL customers.
""")