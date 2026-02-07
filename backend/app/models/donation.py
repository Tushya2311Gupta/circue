from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class DonationRecord(Base):
    __tablename__ = "donation_records"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("assets.id"))
    partner_id: Mapped[str] = mapped_column(String(36), ForeignKey("partners.id"))
    donation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    impact_notes: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
