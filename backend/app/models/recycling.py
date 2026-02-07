from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class RecyclingRecord(Base):
    __tablename__ = "recycling_records"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("assets.id"))
    partner_id: Mapped[str] = mapped_column(String(36), ForeignKey("partners.id"))
    recycle_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    certificate_id: Mapped[str] = mapped_column(String(255), default="")
    compliant: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
