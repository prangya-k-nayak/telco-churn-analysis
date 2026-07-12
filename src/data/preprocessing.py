"""Utilities for preprocessing the Telco Customer Churn dataset."""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_telco_churn_data(data: pd.DataFrame) -> pd.DataFrame:
    """Apply the notebook's preprocessing steps to Telco churn data.

    The function copies the input data, removes the customer identifier,
    converts ``TotalCharges`` to numeric values, fills missing
    ``TotalCharges`` values with the median, and label-encodes every
    object-typed column.

    Args:
        data: Raw Telco churn dataset.

    Returns:
        The preprocessed dataset.
    """
    data = data.copy()
    data = data.drop("customerID", axis=1)

    data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    data["TotalCharges"] = data["TotalCharges"].fillna(
        data["TotalCharges"].median()
    )

    for column in data.columns:
        if data[column].dtype == "object":
            label_encoder = LabelEncoder()
            data[column] = label_encoder.fit_transform(data[column])

    return data
