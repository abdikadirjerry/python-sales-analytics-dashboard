"""Streamlit sidebar filters component."""

import pandas as pd
import streamlit as st


def render_sidebar_filters(df: pd.DataFrame) -> tuple[pd.DataFrame, str, object]:
    """Render sidebar filters for data source, date range, region, and category."""
    st.sidebar.header("📊 Data & Filters")

    # Data Source selection
    data_source_option = st.sidebar.selectbox(
        "Select Data Source",
        options=["Synthetic Sample Data", "Upload CSV"],
        index=0,
    )
    
    source_key = "synthetic" if data_source_option == "Synthetic Sample Data" else "upload"
    uploaded_file = None
    if source_key == "upload":
        uploaded_file = st.sidebar.file_uploader("Upload Sales CSV", type=["csv"])

    if df.empty:
        return df, source_key, uploaded_file

    st.sidebar.divider()
    st.sidebar.subheader("Filter Transactions")

    # Date range filter
    min_date = pd.to_datetime(df["order_date"]).min().date()
    max_date = pd.to_datetime(df["order_date"]).max().date()

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    # Region filter
    regions = sorted(df["region"].unique().tolist())
    selected_regions = st.sidebar.multiselect("Region", options=regions, default=regions)

    # Category filter
    categories = sorted(df["category"].unique().tolist())
    selected_categories = st.sidebar.multiselect("Category", options=categories, default=categories)

    # Apply filters
    filtered_df = df.copy()
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (pd.to_datetime(filtered_df["order_date"]).dt.date >= start_date)
            & (pd.to_datetime(filtered_df["order_date"]).dt.date <= end_date)
        ]

    if selected_regions:
        filtered_df = filtered_df[filtered_df["region"].isin(selected_regions)]

    if selected_categories:
        filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]

    return filtered_df, source_key, uploaded_file