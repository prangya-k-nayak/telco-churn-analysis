import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

    html, body, [class*="css"]{
        font-family: 'Inter', sans-serif;
    }

    h1,h2,h3{
        font-family:'Space Grotesk',sans-serif;
    }

    </style>
    """, unsafe_allow_html=True)