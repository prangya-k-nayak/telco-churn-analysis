import joblib
from pathlib import Path


def save_model(model, filename):
    """Save a trained model to the models folder."""

    model_dir = Path(__file__).resolve().parents[2] / "models"
    model_dir.mkdir(exist_ok=True)

    joblib.dump(model, model_dir / filename)