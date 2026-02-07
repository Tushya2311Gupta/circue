from datetime import datetime
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    asset_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    input_features: Mapped[str] = mapped_column(String(2000))
    risk_level: Mapped[str] = mapped_column(String(16))
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    recommended_action: Mapped[str] = mapped_column(String(32))
    model_version: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
