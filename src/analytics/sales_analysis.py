"""Module for aggregating sales trends, categories, and top products."""

import pandas as pd


def get_revenue_over_time(df: pd.DataFrame, freq: str = "D") -> pd.DataFrame:
    """Aggregate revenue over time by specified frequency (D = Daily, W = Weekly, M = Monthly)."""
    if df.empty or "order_date" not in df.columns or "revenue" not in df.columns:
        return pd.DataFrame(columns=["order_date", "revenue"])

    df_copy = df.copy()
    df_copy["order_date"] = pd.to_datetime(df_copy["order_date"])
    
    # Resample or group by period
    trend = (
        df_copy.set_index("order_date")
        .resample(freq)["revenue"]
        .sum()
        .reset_index()
    )
    return trend


def get_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total revenue and quantity by product category."""
    if df.empty or "category" not in df.columns or "revenue" not in df.columns:
        return pd.DataFrame(columns=["category", "revenue", "quantity"])

    grouped = (
        df.groupby("category", as_index=False)[["revenue", "quantity"]]
        .sum()
        .sort_values(by="revenue", ascending=False)
    )
    return grouped


def get_top_products(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Get the top N best-selling products by revenue."""
    if df.empty or "product_name" not in df.columns or "revenue" not in df.columns:
        return pd.DataFrame(columns=["product_name", "category", "revenue", "quantity"])

    grouped = (
        df.groupby(["product_name", "category"], as_index=False)[["revenue", "quantity"]]
        .sum()
        .sort_values(by="revenue", ascending=False)
        .head(n)
    )
    return grouped