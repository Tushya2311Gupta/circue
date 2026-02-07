import uuid
from datetime import date
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.esg import ESGMetric
from app.schemas.esg import ESGMetricCreate, ESGMetricOut
from app.services.esg import calculate_esg_snapshot


router = APIRouter(prefix="/esg", tags=["esg"])


@router.get("/metrics", response_model=list[ESGMetricOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_metrics(db: Session = Depends(get_db)):
    return db.query(ESGMetric).order_by(ESGMetric.period_start.desc()).all()


@router.post("/metrics", response_model=ESGMetricOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_metric(payload: ESGMetricCreate, db: Session = Depends(get_db)):
    metric = ESGMetric(id=str(uuid.uuid4()), **payload.model_dump())
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric


@router.get("/snapshot", dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def snapshot(
    period_start: date = Query(...),
    period_end: date = Query(...),
    db: Session = Depends(get_db),
):
    return calculate_esg_snapshot(db, period_start, period_end)
