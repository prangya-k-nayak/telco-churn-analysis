import joblib
from pathlib import Path


def load_model(filename):
    """Load a trained model from the models folder."""

    model_dir = Path(__file__).resolve().parents[2] / "models"

    return joblib.load(model_dir / filename)