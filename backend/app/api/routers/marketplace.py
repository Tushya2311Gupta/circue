import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.marketplace import MarketplaceListing, ListingStatus
from app.schemas.marketplace import MarketplaceListingCreate, MarketplaceListingOut


router = APIRouter(prefix="/marketplace", tags=["marketplace"])


@router.get("/listings", response_model=list[MarketplaceListingOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_listings(db: Session = Depends(get_db)):
    return db.query(MarketplaceListing).all()


@router.post("/listings", response_model=MarketplaceListingOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_listing(payload: MarketplaceListingCreate, db: Session = Depends(get_db)):
    listing = MarketplaceListing(
        id=str(uuid.uuid4()),
        asset_id=payload.asset_id,
        listing_status=ListingStatus(payload.listing_status),
        asking_price=payload.asking_price,
        available_from=payload.available_from or datetime.utcnow(),
        reserved_by=payload.reserved_by,
    )
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


@router.put("/listings/{listing_id}", response_model=MarketplaceListingOut, dependencies=[Depends(require_roles("admin", "manager"))])
def update_listing(listing_id: str, payload: MarketplaceListingCreate, db: Session = Depends(get_db)):
    listing = db.get(MarketplaceListing, listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    listing.listing_status = ListingStatus(payload.listing_status)
    listing.asking_price = payload.asking_price
    listing.available_from = payload.available_from or listing.available_from
    listing.reserved_by = payload.reserved_by
    db.commit()
    db.refresh(listing)
    return listing
