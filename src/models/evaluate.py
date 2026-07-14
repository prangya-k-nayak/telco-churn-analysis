"""Model-evaluation utilities for Telco churn prediction."""

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import classification_report

TargetVector = pd.Series | NDArray[np.int64]


def evaluate_model(
    y_true: TargetVector,
    y_pred: TargetVector,
) -> tuple[float, str, NDArray[np.int64]]:
    """Calculate classification metrics for model predictions.

    Args:
        y_true: Actual churn labels.
        y_pred: Predicted churn labels.

    Returns:
        A tuple containing the accuracy score, classification report, and
        confusion matrix, in that order.
    """
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true,y_pred,output_dict=True)
    matrix = confusion_matrix(y_true, y_pred)

    return accuracy, report, matrix
