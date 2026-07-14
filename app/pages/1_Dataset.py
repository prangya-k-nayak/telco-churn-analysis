import streamlit as st
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.data.loader import load_telco_churn_data

st.set_page_config(page_title="Dataset", page_icon="📊")

df = load_telco_churn_data()

st.title("📊 Dataset Overview")

st.markdown("Explore the Telecom Customer Churn dataset.")

# ---------------- Metrics ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.divider()

# ---------------- Preview ----------------

st.subheader("Dataset Preview")

rows = st.slider(
    "Number of rows",
    min_value=5,
    max_value=50,
    value=10,
)

st.dataframe(df.head(rows), width="stretch")

st.divider()

# ---------------- Column Information ----------------

st.subheader("Column Information")

info = df.dtypes.astype(str).reset_index()
info.columns = ["Column", "Data Type"]

st.dataframe(info, width="stretch")

st.divider()

# ---------------- Missing Values ----------------

st.subheader("Missing Values")

missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]

st.dataframe(missing, width="stretch")

st.divider()

# ---------------- Download ----------------

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="Telco-Customer-Churn.csv",
    mime="text/csv",
)