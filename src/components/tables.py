"""Streamlit data table and export component."""

import pandas as pd
import streamlit as st


def render_sales_table(filtered_df: pd.DataFrame) -> None:
    """Render filtered transactions table with CSV download option."""
    st.subheader("📋 Filtered Sales Transactions")
    
    if filtered_df.empty:
        st.warning("No transactions match the selected filters.")
        return

    st.dataframe(filtered_df, use_container_width=True)

    # CSV Export
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_sales_data.csv",
        mime="text/csv",
    )