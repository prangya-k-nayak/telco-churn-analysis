"""Utilities for loading project datasets."""

from pathlib import Path

import pandas as pd


def load_telco_churn_data() -> pd.DataFrame:
    """Load the Telco Customer Churn dataset from the project's raw-data folder.

    Returns:
        The Telco Customer Churn dataset as a pandas DataFrame.

    Raises:
        FileNotFoundError: If data/raw/Telco-Customer-Churn.csv does not exist.
    """
    project_root = Path(__file__).resolve().parents[2]
    dataset_path = project_root / "data" / "raw" / "Telco-Customer-Churn.csv"

    if not dataset_path.is_file():
        raise FileNotFoundError(
            f"Telco churn dataset not found at: {dataset_path}. "
            "Expected data/raw/Telco-Customer-Churn.csv."
        )

    return pd.read_csv(dataset_path)
