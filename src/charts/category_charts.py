"""Category sales breakdown chart generator using Plotly."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_category_sales_chart(category_df: pd.DataFrame) -> go.Figure:
    """Create a bar chart displaying sales revenue by category."""
    if category_df.empty:
        fig = px.bar(title="No Category Data Available")
        return fig

    fig = px.bar(
        category_df,
        x="category",
        y="revenue",
        color="category",
        title="Sales Revenue by Category",
        text_auto=".2s",
        labels={"category": "Product Category", "revenue": "Revenue ($)"},
    )
    fig.update_layout(
        template="plotly_white",
        xaxis_title="Category",
        yaxis_title="Revenue ($)",
        showlegend=False,
    )
    return fig