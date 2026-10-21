"""Unit tests for KPI calculations and sales aggregation functions."""

import pandas as pd
import pytest
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


@pytest.fixture
def sample_sales_df():
    """Fixture providing a small, controlled sample DataFrame for testing."""
    return pd.DataFrame({
        "order_id": ["ORD-1", "ORD-1", "ORD-2", "ORD-3"],
        "order_date": pd.to_datetime(["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-03"]),
        "customer_id": ["C-1", "C-1", "C-2", "C-3"],
        "region": ["North", "North", "South", "East"],
        "category": ["Electronics", "Electronics", "Apparel", "Home"],
        "product_name": ["Mouse", "Mouse", "Hoodie", "Blender"],
        "unit_price": [25.0, 25.0, 50.0, 100.0],
        "quantity": [2, 1, 1, 2],
        "revenue": [50.0, 25.0, 50.0, 200.0]
    })


def test_kpi_calculations(sample_sales_df):
    """Test core KPI functions with sample data."""
    assert calculate_total_revenue(sample_sales_df) == 325.0
    assert calculate_total_orders(sample_sales_df) == 3  # ORD-1, ORD-2, ORD-3
    assert calculate_average_order_value(sample_sales_df) == 325.0 / 3
    assert calculate_total_units_sold(sample_sales_df) == 6  # 2 + 1 + 1 + 2


def test_kpi_empty_dataframe():
    """Test KPI calculations with an empty DataFrame edge case."""
    empty_df = pd.DataFrame()
    assert calculate_total_revenue(empty_df) == 0.0
    assert calculate_total_orders(empty_df) == 0
    assert calculate_average_order_value(empty_df) == 0.0
    assert calculate_total_units_sold(empty_df) == 0


def test_sales_by_category(sample_sales_df):
    """Test category aggregation."""
    cat_df = get_sales_by_category(sample_sales_df)
    assert not cat_df.empty
    home_row = cat_df[cat_df["category"] == "Home"]
    assert float(home_row["revenue"].values[0]) == 200.0


def test_top_products(sample_sales_df):
    """Test top products aggregation."""
    top_df = get_top_products(sample_sales_df, n=2)
    assert len(top_df) <= 2
    assert top_df.iloc[0]["product_name"] == "Blender"