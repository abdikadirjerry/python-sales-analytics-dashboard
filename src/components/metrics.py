"""Streamlit KPI metric cards component."""

import streamlit as st


def render_kpi_metrics(total_rev: int | float, total_orders: int, aov: float, units_sold: int) -> None:
    """Render top-level summary KPI metric cards in Streamlit columns."""
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Revenue", value=f"${total_rev:,.2f}")
    with col2:
        st.metric(label="Total Orders", value=f"{total_orders:,}")
    with col3:
        st.metric(label="Avg Order Value (AOV)", value=f"${aov:,.2f}")
    with col4:
        st.metric(label="Total Units Sold", value=f"{units_sold:,}")