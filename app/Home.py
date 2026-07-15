import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from src.ui.styles import apply_theme
from src.data.loader import load_telco_churn_data

st.set_page_config(
    page_title="Telecom Customer Churn Dashboard",
    page_icon="📊",
    layout="wide",
)
apply_theme()

df = load_telco_churn_data()

st.title("📊 Telecom Customer Churn Dashboard")

st.markdown("""
Welcome to the **Telecom Customer Churn Dashboard**.

Use the **pages in the sidebar** to explore the dataset, perform EDA,
view model performance, and predict customer churn.
""")

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(df))
col2.metric("Features", df.shape[1] - 1)
col3.metric("Churn Rate", f"{(df['Churn'] == 'Yes').mean() * 100:.1f}%")

st.success("👈 Select a page from the sidebar.")