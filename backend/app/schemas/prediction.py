from datetime import datetime
from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    raw_material_kg: float = Field(..., ge=0)
    recycled_material_kg: float = Field(..., ge=0)
    waste_kg: float = Field(..., ge=0)
    energy_kwh: float = Field(..., ge=0)
    water_liters: float = Field(..., ge=0)
    machine_downtime_min: float = Field(..., ge=0)
    production_volume_units: float = Field(..., ge=0)
    material_recovery_rate: float = Field(..., ge=0, le=1)
    circularity_score: float = Field(..., ge=0, le=100)


class PredictionResponse(BaseModel):
    risk_level: str
    confidence: float
    recommended_action: str
    model_version: str


class PredictionLogOut(PredictionResponse):
    id: str
    asset_id: str | None
    created_at: datetime

    class Config:
        from_attributes = True
