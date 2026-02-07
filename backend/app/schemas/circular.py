from datetime import datetime
from pydantic import BaseModel


class DonationCreate(BaseModel):
    asset_id: str
    partner_id: str
    donation_date: datetime | None = None
    impact_notes: str = ""


class DonationOut(DonationCreate):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


class RecyclingCreate(BaseModel):
    asset_id: str
    partner_id: str
    recycle_date: datetime | None = None
    certificate_id: str = ""
    compliant: bool = True


class RecyclingOut(RecyclingCreate):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
