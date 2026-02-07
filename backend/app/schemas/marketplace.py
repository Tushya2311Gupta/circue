from datetime import datetime
from pydantic import BaseModel


class MarketplaceListingBase(BaseModel):
    asset_id: str
    listing_status: str = "available"
    asking_price: float = 0
    available_from: datetime | None = None
    reserved_by: str = ""


class MarketplaceListingCreate(MarketplaceListingBase):
    pass


class MarketplaceListingOut(MarketplaceListingBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
