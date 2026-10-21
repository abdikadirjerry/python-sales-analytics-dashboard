"""Data loading module supporting synthetic generation and CSV uploads."""

import pandas as pd
from src.data.sample_data import generate_sample_sales_data


def load_data(source: str = "synthetic", uploaded_file=None) -> pd.DataFrame:
    """Load sales data based on the selected source."""
    if source == "synthetic":
        return generate_sample_sales_data()
    elif source == "upload" and uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            raise ValueError(f"Failed to parse uploaded CSV file: {e}")
    else:
        raise ValueError("Invalid data source or missing uploaded file.")