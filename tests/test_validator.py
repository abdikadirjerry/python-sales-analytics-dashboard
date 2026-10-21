"""Unit tests for data validation and cleaning logic."""

import pandas as pd
from src.data.validator import clean_sales_data, validate_schema


def test_validate_schema_valid():
    """Test schema validation with a correctly formatted DataFrame."""
    df = pd.DataFrame(columns=[
        "order_id", "order_date", "customer_id", "region",
        "category", "product_name", "unit_price", "quantity", "revenue"
    ])
    is_valid, errors = validate_schema(df)
    assert is_valid is True
    assert len(errors) == 0


def test_validate_schema_missing_columns():
    """Test schema validation when required columns are missing."""
    df = pd.DataFrame(columns=["order_id", "order_date"])
    is_valid, errors = validate_schema(df)
    assert is_valid is False
    assert len(errors) > 0


def test_clean_sales_data():
    """Test cleaning logic for duplicates, bad dates, and NaNs."""
    data = {
        "order_id": ["ORD-1", "ORD-1", "ORD-3"],
        "order_date": ["2026-01-01", "2026-01-01", "invalid-date"],
        "customer_id": ["CUST-1", "CUST-1", "CUST-3"],
        "region": ["North", "North", "South"],
        "category": ["Tech", "Tech", "Home"],
        "product_name": ["Mouse", "Mouse", "Blender"],
        "unit_price": [20.0, 20.0, None],
        "quantity": [2, 2, 1],
        "revenue": [40.0, 40.0, 0.0]
    }
    df = pd.DataFrame(data)
    cleaned_df = clean_sales_data(df)

    # Should drop duplicate row (ORD-1) and invalid date row (ORD-3)
    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["order_id"] == "ORD-1"