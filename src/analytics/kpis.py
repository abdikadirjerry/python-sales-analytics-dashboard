"""Module for computing core sales Key Performance Indicators (KPIs)."""

import pandas as pd


def calculate_total_revenue(df: pd.DataFrame) -> float:
    """Calculate total sales revenue from valid transactions."""
    if df.empty or "revenue" not in df.columns:
        return 0.0
    return float(df["revenue"].sum())


def calculate_total_orders(df: pd.DataFrame) -> int:
    """Calculate total unique orders based on order_id."""
    if df.empty or "order_id" not in df.columns:
        return 0
    return int(df["order_id"].nunique())


def calculate_average_order_value(df: pd.DataFrame) -> float:
    """Calculate average order value (Total Revenue / Unique Orders)."""
    total_revenue = calculate_total_revenue(df)
    total_orders = calculate_total_orders(df)
    if total_orders == 0:
        return 0.0
    return float(total_revenue / total_orders)


def calculate_total_units_sold(df: pd.DataFrame) -> int:
    """Calculate total unit quantity sold."""
    if df.empty or "quantity" not in df.columns:
        return 0
    return int(df["quantity"].sum())