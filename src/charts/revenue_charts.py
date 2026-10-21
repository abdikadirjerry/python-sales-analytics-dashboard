"""Revenue over time chart generator using Plotly."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_revenue_trend_chart(trend_df: pd.DataFrame) -> go.Figure:
    """Create an interactive line chart for revenue trends over time."""
    if trend_df.empty:
        fig = px.line(title="No Revenue Data Available")
        return fig

    fig = px.line(
        trend_df,
        x="order_date",
        y="revenue",
        title="Revenue Trend Over Time",
        markers=True,
        labels={"order_date": "Date", "revenue": "Revenue ($)"},
    )
    fig.update_layout(
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title="Revenue ($)",
        hovermode="x unified",
    )
    return fig