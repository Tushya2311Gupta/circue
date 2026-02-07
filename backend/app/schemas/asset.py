from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class AssetBase(BaseModel):
    asset_tag: str
    name: str
    category: str
    manufacturer: str = ""
    model: str = ""
    purchase_date: Optional[date] = None
    location: str = ""
    status: str = "purchased"
    usage_hours: float = 0
    energy_kwh: float = 0
    waste_kg: float = 0
    recycled_material_kg: float = 0
    raw_material_kg: float = 0
    water_liters: float = 0
    circularity_score: float = 0


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    purchase_date: Optional[date] = None
    location: Optional[str] = None
    status: Optional[str] = None
    usage_hours: Optional[float] = None
    energy_kwh: Optional[float] = None
    waste_kg: Optional[float] = None
    recycled_material_kg: Optional[float] = None
    raw_material_kg: Optional[float] = None
    water_liters: Optional[float] = None
    circularity_score: Optional[float] = None


class AssetOut(AssetBase):
    id: str
    carbon_kg: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LifecycleEventCreate(BaseModel):
    event_type: str
    event_date: Optional[datetime] = None
    details: str = ""
    performed_by: str = "system"


class LifecycleEventOut(BaseModel):
    id: str
    asset_id: str
    event_type: str
    event_date: datetime
    details: str
    performed_by: str
    created_at: datetime

    class Config:
        from_attributes = True


class CSVUploadResult(BaseModel):
    created: int
    failed: int
    errors: list[str] = []
