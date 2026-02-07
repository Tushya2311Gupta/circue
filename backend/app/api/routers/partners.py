import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.partner import Partner, PartnerType
from app.schemas.partner import PartnerCreate, PartnerOut


router = APIRouter(prefix="/partners", tags=["partners"])


@router.get("", response_model=list[PartnerOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_partners(db: Session = Depends(get_db)):
    return db.query(Partner).all()


@router.post("", response_model=PartnerOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_partner(payload: PartnerCreate, db: Session = Depends(get_db)):
    partner = Partner(
        id=str(uuid.uuid4()),
        name=payload.name,
        partner_type=PartnerType(payload.partner_type),
        contact_email=payload.contact_email,
        phone=payload.phone,
        address=payload.address,
        certifications=payload.certifications,
        compliance_rating=payload.compliance_rating,
    )
    db.add(partner)
    db.commit()
    db.refresh(partner)
    return partner


@router.put("/{partner_id}", response_model=PartnerOut, dependencies=[Depends(require_roles("admin", "manager"))])
def update_partner(partner_id: str, payload: PartnerCreate, db: Session = Depends(get_db)):
    partner = db.get(Partner, partner_id)
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    partner.name = payload.name
    partner.partner_type = PartnerType(payload.partner_type)
    partner.contact_email = payload.contact_email
    partner.phone = payload.phone
    partner.address = payload.address
    partner.certifications = payload.certifications
    partner.compliance_rating = payload.compliance_rating
    db.commit()
    db.refresh(partner)
    return partner
