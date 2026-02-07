from dataclasses import dataclass

import numpy as np

from app.ml.model_loader import load_model


FEATURE_ORDER = [
    "raw_material_kg",
    "recycled_material_kg",
    "waste_kg",
    "energy_kwh",
    "water_liters",
    "machine_downtime_min",
    "production_volume_units",
    "material_recovery_rate",
    "circularity_score",
]


@dataclass
class PredictionResult:
    risk_level: str
    confidence: float
    recommended_action: str
    model_version: str


def _recommend_action(risk_level: str, circularity_score: float, recovery_rate: float) -> str:
    if risk_level == "high":
        if circularity_score < 40 or recovery_rate < 0.4:
            return "Recycle"
        if circularity_score < 60:
            return "Refurbish"
        return "Repair"
    if circularity_score >= 75:
        return "Redeploy"
    return "Repair"


def predict_waste_risk(features: dict[str, float]) -> PredictionResult:
    artifacts = load_model()
    model = artifacts.model

    values = [features[name] for name in FEATURE_ORDER]
    payload = np.array(values).reshape(1, -1)

    probas = model.predict_proba(payload)
    high_risk_proba = float(probas[0][1])
    risk_level = "high" if high_risk_proba >= 0.5 else "low"
    confidence = high_risk_proba if risk_level == "high" else 1 - high_risk_proba
    recommended_action = _recommend_action(
        risk_level,
        features["circularity_score"],
        features["material_recovery_rate"],
    )

    return PredictionResult(
        risk_level=risk_level,
        confidence=round(confidence, 4),
        recommended_action=recommended_action,
        model_version=artifacts.model_version,
    )
