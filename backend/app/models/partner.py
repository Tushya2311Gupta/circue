import enum
from datetime import datetime
from sqlalchemy import DateTime, Enum, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class PartnerType(str, enum.Enum):
    refurbisher = "refurbisher"
    recycler = "recycler"
    donor = "donor"


class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    partner_type: Mapped[PartnerType] = mapped_column(Enum(PartnerType, native_enum=False))
    contact_email: Mapped[str] = mapped_column(String(255), default="")
    phone: Mapped[str] = mapped_column(String(64), default="")
    address: Mapped[str] = mapped_column(String(500), default="")
    certifications: Mapped[str] = mapped_column(String(1000), default="")
    compliance_rating: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
