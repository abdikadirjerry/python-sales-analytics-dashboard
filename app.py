"""Main entry point for the Sales Analytics Dashboard Streamlit application."""

import streamlit as st
from src.analytics.kpis import (
    calculate_average_order_value,
    calculate_total_orders,
    calculate_total_revenue,
    calculate_total_units_sold,
)
from src.analytics.sales_analysis import (
    get_revenue_over_time,
    get_sales_by_category,
    get_top_products,
)
from src.charts.category_charts import create_category_sales_chart
from src.charts.revenue_charts import create_revenue_trend_chart
from src.components.filters import render_sidebar_filters
from src.components.metrics import render_kpi_metrics
from src.components.tables import render_sales_table
from src.data.loader import load_data
from src.data.validator import clean_sales_data, validate_schema

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Sales Analytics Dashboard")
st.markdown("Monitor revenue trends, product category performance, and key metrics in real time.")

# Load raw data based on sidebar selection
# We initialize with synthetic first to get initial bounds for filters
initial_df = load_data(source="synthetic")
cleaned_initial_df = clean_sales_data(initial_df)

filtered_df, source_key, uploaded_file = render_sidebar_filters(cleaned_initial_df)

# Handle custom CSV upload if selected
if source_key == "upload":
    if uploaded_file is not None:
        try:
            raw_uploaded_df = load_data(source="upload", uploaded_file=uploaded_file)
            is_valid, errors = validate_schema(raw_uploaded_df)
            if not is_valid:
                st.error("Uploaded CSV schema is invalid:")
                for err in errors:
                    st.error(f"- {err}")
                st.stop()
            cleaned_uploaded_df = clean_sales_data(raw_uploaded_df)
            # Re-render filters with uploaded data
            filtered_df, _, _ = render_sidebar_filters(cleaned_uploaded_df)
        except Exception as e:
            st.error(f"Error processing uploaded file: {e}")
            st.stop()
    else:
        st.info("Please upload a CSV file in the sidebar to begin analysis.")
        st.stop()

st.divider()

# Compute KPIs
total_rev = calculate_total_revenue(filtered_df)
total_orders = calculate_total_orders(filtered_df)
aov = calculate_average_order_value(filtered_df)
units_sold = calculate_total_units_sold(filtered_df)

# Render KPI metric cards
render_kpi_metrics(total_rev, total_orders, aov, units_sold)

st.divider()

# Render Visualizations
col_left, col_right = st.columns(2)

with col_left:
    trend_data = get_revenue_over_time(filtered_df, freq="D")
    revenue_fig = create_revenue_trend_chart(trend_data)
    st.plotly_chart(revenue_fig, use_container_width=True)

with col_right:
    category_data = get_sales_by_category(filtered_df)
    category_fig = create_category_sales_chart(category_data)
    st.plotly_chart(category_fig, use_container_width=True)

st.divider()

# Top products summary section
st.subheader("🏆 Top Performing Products")
top_products_df = get_top_products(filtered_df, n=5)
if not top_products_df.empty:
    st.dataframe(top_products_df, use_container_width=True)
else:
    st.info("No product data available for the selected filters.")

st.divider()

# Render filtered table and export
render_sales_table(filtered_df)