import streamlit as st

def info_card(title, value, subtitle):
    st.markdown(f"""
    <div class="card">
        <h4>{title}</h4>
        <h2>{value}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)