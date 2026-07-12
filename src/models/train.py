"""Model-training utilities for Telco churn prediction."""

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

FeatureMatrix = pd.DataFrame | NDArray[np.float64]
TargetVector = pd.Series | NDArray[np.int64]


def train_logistic_regression(
    features: FeatureMatrix,
    target: TargetVector,
    *,
    max_iter: int = 1000,
) -> LogisticRegression:
    """Train a Logistic Regression model for churn prediction.

    Args:
        features: Training feature matrix.
        target: Training target values.
        max_iter: Maximum number of optimization iterations.

    Returns:
        The fitted Logistic Regression model.
    """
    model = LogisticRegression(max_iter=max_iter)
    model.fit(features, target)
    return model


def train_random_forest(
    features: FeatureMatrix,
    target: TargetVector,
    *,
    random_state: int | None = 42,
) -> RandomForestClassifier:
    """Train a Random Forest model for churn prediction.

    Args:
        features: Training feature matrix.
        target: Training target values.
        random_state: Seed used to make training reproducible.

    Returns:
        The fitted Random Forest model.
    """
    model = RandomForestClassifier(random_state=random_state)
    model.fit(features, target)
    return model
