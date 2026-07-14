import streamlit as st
import sys
from pathlib import Path
import plotly.express as px

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.data.loader import load_telco_churn_data

st.set_page_config(page_title="EDA", page_icon="📈")

df = load_telco_churn_data()

st.title("📈 Exploratory Data Analysis")

st.markdown("Interactive visualizations of the Telecom Customer Churn dataset.")

# -----------------------------
# Churn Distribution
# -----------------------------
st.subheader("Customer Churn Distribution")

fig = px.histogram(
    df,
    x="Churn",
    color="Churn",
    text_auto=True,
)

st.plotly_chart(fig, width="stretch")

# -----------------------------
# Gender vs Churn
# -----------------------------
st.subheader("Gender vs Churn")

fig = px.histogram(
    df,
    x="gender",
    color="Churn",
    barmode="group",
)

st.plotly_chart(fig, width="stretch")

# -----------------------------
# Contract vs Churn
# -----------------------------
st.subheader("Contract Type vs Churn")

fig = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
)

st.plotly_chart(fig, width="stretch")