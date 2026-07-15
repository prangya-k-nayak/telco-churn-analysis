import streamlit as st


def page_header(title: str, subtitle: str):
    """Reusable page header."""

    st.title(title)
    st.caption(subtitle)