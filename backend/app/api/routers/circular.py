import uuid
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.asset import Asset, LifecycleStatus
from app.models.donation import DonationRecord
from app.models.recycling import RecyclingRecord
from app.schemas.circular import DonationCreate, DonationOut, RecyclingCreate, RecyclingOut


router = APIRouter(prefix="/circular", tags=["circular"])


@router.get("/donations", response_model=list[DonationOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_donations(db: Session = Depends(get_db)):
    return db.query(DonationRecord).all()


@router.post("/donations", response_model=DonationOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_donation(payload: DonationCreate, db: Session = Depends(get_db)):
    record = DonationRecord(
        id=str(uuid.uuid4()),
        asset_id=payload.asset_id,
        partner_id=payload.partner_id,
        donation_date=payload.donation_date or datetime.utcnow(),
        impact_notes=payload.impact_notes,
    )
    asset = db.get(Asset, payload.asset_id)
    if asset:
        asset.status = LifecycleStatus.reuse
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/recycling", response_model=list[RecyclingOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_recycling(db: Session = Depends(get_db)):
    return db.query(RecyclingRecord).all()


@router.post("/recycling", response_model=RecyclingOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_recycling(payload: RecyclingCreate, db: Session = Depends(get_db)):
    record = RecyclingRecord(
        id=str(uuid.uuid4()),
        asset_id=payload.asset_id,
        partner_id=payload.partner_id,
        recycle_date=payload.recycle_date or datetime.utcnow(),
        certificate_id=payload.certificate_id,
        compliant=payload.compliant,
    )
    asset = db.get(Asset, payload.asset_id)
    if asset:
        asset.status = LifecycleStatus.recycle
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
