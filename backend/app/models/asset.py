import enum
from datetime import date, datetime
from sqlalchemy import Date, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class AssetCategory(str, enum.Enum):
    laptop = "laptop"
    server = "server"
    network_device = "network_device"
    peripheral = "peripheral"


class LifecycleStatus(str, enum.Enum):
    purchased = "purchased"
    in_use = "in_use"
    repair = "repair"
    reuse = "reuse"
    refurbish = "refurbish"
    recycle = "recycle"
    retired = "retired"


class LifecycleEventType(str, enum.Enum):
    purchase = "purchase"
    use = "use"
    repair = "repair"
    reuse = "reuse"
    refurbish = "refurbish"
    recycle = "recycle"
    retire = "retire"
    donate = "donate"


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_tag: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    category: Mapped[AssetCategory] = mapped_column(Enum(AssetCategory, native_enum=False), index=True)
    manufacturer: Mapped[str] = mapped_column(String(255), default="")
    model: Mapped[str] = mapped_column(String(255), default="")
    purchase_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    location: Mapped[str] = mapped_column(String(255), default="")
    status: Mapped[LifecycleStatus] = mapped_column(Enum(LifecycleStatus, native_enum=False), default=LifecycleStatus.purchased)

    usage_hours: Mapped[float] = mapped_column(Float, default=0.0)
    energy_kwh: Mapped[float] = mapped_column(Float, default=0.0)
    waste_kg: Mapped[float] = mapped_column(Float, default=0.0)
    recycled_material_kg: Mapped[float] = mapped_column(Float, default=0.0)
    raw_material_kg: Mapped[float] = mapped_column(Float, default=0.0)
    water_liters: Mapped[float] = mapped_column(Float, default=0.0)
    circularity_score: Mapped[float] = mapped_column(Float, default=0.0)
    carbon_kg: Mapped[float] = mapped_column(Float, default=0.0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    lifecycle_events: Mapped[list["LifecycleEvent"]] = relationship("LifecycleEvent", back_populates="asset")


class LifecycleEvent(Base):
    __tablename__ = "lifecycle_events"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("assets.id"), index=True)
    event_type: Mapped[LifecycleEventType] = mapped_column(Enum(LifecycleEventType, native_enum=False))
    event_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    details: Mapped[str] = mapped_column(String(1000), default="")
    performed_by: Mapped[str] = mapped_column(String(255), default="system")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    asset: Mapped[Asset] = relationship("Asset", back_populates="lifecycle_events")
