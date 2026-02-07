from datetime import date, datetime
from pydantic import BaseModel


class ESGMetricCreate(BaseModel):
    period_start: date
    period_end: date
    scope3_emissions_kg: float
    circularity_index: float
    waste_diverted_kg: float
    recycled_materials_kg: float
    sdg12_alignment: float
    sdg17_alignment: float


class ESGMetricOut(ESGMetricCreate):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
