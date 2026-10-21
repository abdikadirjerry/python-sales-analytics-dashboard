"""Main entry point for the Sales Analytics Dashboard Streamlit application."""

import streamlit as st

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Sales Analytics Dashboard")
st.markdown("Welcome to your professional Python sales analytics application.")

st.info(
    "Part 1 complete: Environment, project structure, and dependencies are successfully configured."
)

if st.button("Test Interactive State"):
    st.success("Streamlit interactive state is working correctly!")