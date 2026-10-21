"""Module for generating reproducible synthetic sales data."""

import numpy as np
import pandas as pd


def generate_sample_sales_data(num_rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Generate a synthetic sales transactions DataFrame for testing and development."""
    np.random.seed(seed)

    # Date range over the past year
    end_date = pd.Timestamp.today().normalize()
    start_date = end_date - pd.Timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq="h")

    order_dates = np.random.choice(dates, size=num_rows)

    categories_products = {
        "Electronics": ["Wireless Mouse", "Mechanical Keyboard", "Monitor", "USB-C Hub", "Webcam"],
        "Apparel": ["Running Shoes", "Cotton Hoodie", "Waterproof Jacket", "Graphic Tee", "Wool Socks"],
        "Home & Kitchen": ["Air Fryer", "Coffee Maker", "Blender", "Cast Iron Skillet", "Electric Kettle"],
        "Office Supplies": ["Standing Desk", "Ergonomic Chair", "Desk Lamp", "Notebook Set", "Gel Pens"]
    }

    categories = list(categories_products.keys())
    selected_categories = np.random.choice(categories, size=num_rows)
    
    products = [
        np.random.choice(categories_products[cat]) for cat in selected_categories
    ]

    unit_prices = {
        "Wireless Mouse": 29.99, "MechanicalKeyboard": 89.99, "Monitor": 249.99, "USB-C Hub": 39.99, "Webcam": 59.99,
        "Running Shoes": 79.99, "Cotton Hoodie": 49.99, "Waterproof Jacket": 119.99, "Graphic Tee": 24.99, "Wool Socks": 14.99,
        "Air Fryer": 99.99, "Coffee Maker": 79.99, "Blender": 49.99, "Cast Iron Skillet": 39.99, "Electric Kettle": 45.99,
        "Standing Desk": 299.99, "Ergonomic Chair": 199.99, "Desk Lamp": 34.99, "Notebook Set": 12.99, "Gel Pens": 9.99
    }

    prices = [unit_prices.get(p, 49.99) for p in products]
    quantities = np.random.randint(1, 6, size=num_rows)
    regions = np.random.choice(["North", "South", "East", "West", "Central"], size=num_rows)
    customer_ids = [f"CUST-{np.random.randint(1000, 1500)}" for _ in range(num_rows)]
    order_ids = [f"ORD-{2026}-{i:05d}" for i in range(num_rows)]

    df = pd.DataFrame({
        "order_id": order_ids,
        "order_date": order_dates,
        "customer_id": customer_ids,
        "region": regions,
        "category": selected_categories,
        "product_name": products,
        "unit_price": prices,
        "quantity": quantities,
    })

    # Calculate total sales revenue per row
    df["revenue"] = df["unit_price"] * df["quantity"]

    return df