import streamlit as st


def metric_card(title: str, value, description: str = ""):
    """Reusable metric card."""

    st.metric(
        label=title,
        value=value,
        help=description if description else None,
    )