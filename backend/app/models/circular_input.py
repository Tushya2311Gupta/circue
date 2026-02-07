from pydantic import BaseModel, Field


class CircularInput(BaseModel):
    production_volume_units: int = Field(..., gt=0)
    raw_material_kg: float = Field(..., gt=0)
    recycled_material_kg: float = Field(..., ge=0)
    energy_kwh: float = Field(..., gt=0)
    water_liters: float = Field(..., gt=0)
    machine_downtime_min: int = Field(..., ge=0)
    material_recovery_rate: float = Field(..., ge=0, le=1)
    circularity_score: float = Field(..., ge=0, le=100)
