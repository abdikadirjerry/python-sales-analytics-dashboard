# 📊 Python Sales Analytics Dashboard

An interactive sales analytics dashboard built primarily with Python using Streamlit, Pandas, and Plotly.

The project aims to provide a clear overview of sales performance through key performance indicators, interactive visualizations, data filtering, and reporting.

## Features

Features will be documented here as they are implemented and tested.

Planned capabilities include:

- **KPI metrics:** Revenue, orders, average order value, and units sold.
- **Interactive visualizations:** Revenue trends and category-level sales comparisons.
- **Data sources:** Reproducible synthetic sales data and CSV uploads.
- **Filtering:** Date-range and product-category filters.
- **Reporting:** Sales transaction tables and CSV exports.
- **Code quality:** Automated tests, linting, and modular Python code.

## Technology Stack

- **Language:** Python
- **Web interface:** Streamlit
- **Data processing:** Pandas and NumPy
- **Visualizations:** Plotly
- **Testing:** pytest
- **Linting and formatting:** Ruff
- **Version control:** Git and GitHub

## Project Structure

The architecture will evolve as the project develops. The following is the intended structure:

```text
python-sales-dashboard/
├── app.py
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── analytics/
│   ├── charts/
│   └── components/
├── tests/
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

Individual modules will be added as their corresponding features are implemented.

## Getting Started

### Prerequisites

- Ubuntu on Windows Subsystem for Linux (WSL), or another supported Python environment
- Python 3
- Git

### Installation

Clone the repository after it has been published to GitHub:

```bash
git clone https://github.com/YOUR_USERNAME/python-sales-dashboard.git
cd python-sales-dashboard
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

http://localhost:8501

### Run Tests

Once the automated tests have been implemented and the development dependencies installed, run:

```bash
python -m pytest
```

### Check Code Quality

Once Ruff is configured and installed, run:

```bash
ruff check .
```

## Development Workflow

The project is developed incrementally, with each meaningful feature implemented, tested, and committed separately.

The workflow is:

**Plan → Build → Test → Fix → Review → Commit**

## Deployment

Deployment instructions will be added after the application is ready for deployment.

## Project Status

**Status:** In development.

This project is being built incrementally to develop practical skills in Python application development, data analysis, interactive visualization, software testing, and version control.

## License

A license will be added when one is selected.
