"""Data validation and cleaning module for sales transactions."""

import pandas as pd


EXPECTED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "category",
    "product_name",
    "unit_price",
    "quantity",
    "revenue",
]


def validate_schema(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """Validate that the DataFrame contains all required columns."""
    errors = []
    if not isinstance(df, pd.DataFrame):
        return False, ["Input is not a valid pandas DataFrame."]

    missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing_cols:
        errors.append(f"Missing required columns: {', '.join(missing_cols)}")

    return len(errors) == 0, errors


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean sales data by removing duplicates, handling missing values, and formatting types."""
    df = df.copy()

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    # Parse order_date to datetime, coercing errors to NaT
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df = df.dropna(subset=["order_date"])

    # Ensure numeric types for price, quantity, and revenue
    numeric_cols = ["unit_price", "quantity", "revenue"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    # Re-calculate revenue if needed or ensure consistency
    if "unit_price" in df.columns and "quantity" in df.columns:
        df["revenue"] = df["unit_price"] * df["quantity"]

    # Fill missing categorical values with 'Unknown'
    categorical_cols = ["order_id", "customer_id", "region", "category", "product_name"]
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown").astype(str)

    return df