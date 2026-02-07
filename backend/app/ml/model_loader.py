from pathlib import Path
from typing import Any
import joblib

from app.core.config import get_settings


class ModelArtifacts:
    def __init__(self, model: Any, feature_names: list[str], model_version: str):
        self.model = model
        self.feature_names = feature_names
        self.model_version = model_version


_model_cache: ModelArtifacts | None = None


def load_model() -> ModelArtifacts:
    global _model_cache
    if _model_cache is not None:
        return _model_cache

    settings = get_settings()
    model_path = Path(settings.MODEL_PATH)
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")

    payload = joblib.load(model_path)
    if isinstance(payload, dict) and "model" in payload:
        model = payload["model"]
        feature_names = payload.get("feature_names", [])
        model_version = payload.get("model_version", settings.MODEL_VERSION)
    else:
        model = payload
        feature_names = []
        model_version = settings.MODEL_VERSION

    _model_cache = ModelArtifacts(model=model, feature_names=feature_names, model_version=model_version)
    return _model_cache
