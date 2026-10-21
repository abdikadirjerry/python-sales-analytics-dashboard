"""Unit tests for the data loader and synthetic generator."""

import pandas as pd
from src.data.loader import load_data
from src.data.sample_data import generate_sample_sales_data


def test_generate_sample_sales_data():
    """Test that synthetic data is generated correctly with expected columns."""
    df = generate_sample_sales_data(num_rows=100)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    
    expected_columns = [
        "order_id", "order_date", "customer_id", "region",
        "category", "product_name", "unit_price", "quantity", "revenue"
    ]
    for col in expected_columns:
        assert col in df.columns


def test_load_data_synthetic():
    """Test loading synthetic data via the loader module."""
    df = load_data(source="synthetic")
    assert not df.empty
    assert "revenue" in df.columns