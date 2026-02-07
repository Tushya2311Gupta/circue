import enum
from datetime import datetime
from sqlalchemy import DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class ListingStatus(str, enum.Enum):
    available = "available"
    reserved = "reserved"
    completed = "completed"


class MarketplaceListing(Base):
    __tablename__ = "marketplace_listings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("assets.id"))
    listing_status: Mapped[ListingStatus] = mapped_column(Enum(ListingStatus, native_enum=False), default=ListingStatus.available)
    asking_price: Mapped[float] = mapped_column(Float, default=0.0)
    available_from: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    reserved_by: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
