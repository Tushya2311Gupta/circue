from datetime import date, datetime
from sqlalchemy import Date, DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class ESGMetric(Base):
    __tablename__ = "esg_metrics"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    period_start: Mapped[date] = mapped_column(Date, index=True)
    period_end: Mapped[date] = mapped_column(Date, index=True)
    scope3_emissions_kg: Mapped[float] = mapped_column(Float, default=0.0)
    circularity_index: Mapped[float] = mapped_column(Float, default=0.0)
    waste_diverted_kg: Mapped[float] = mapped_column(Float, default=0.0)
    recycled_materials_kg: Mapped[float] = mapped_column(Float, default=0.0)
    sdg12_alignment: Mapped[float] = mapped_column(Float, default=0.0)
    sdg17_alignment: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
