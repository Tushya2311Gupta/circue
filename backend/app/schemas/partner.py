from datetime import datetime
from pydantic import BaseModel


class PartnerBase(BaseModel):
    name: str
    partner_type: str
    contact_email: str = ""
    phone: str = ""
    address: str = ""
    certifications: str = ""
    compliance_rating: float = 0


class PartnerCreate(PartnerBase):
    pass


class PartnerOut(PartnerBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
