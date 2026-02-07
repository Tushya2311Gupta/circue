import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.asset import Asset, LifecycleEvent, AssetCategory, LifecycleStatus, LifecycleEventType
from app.schemas.asset import (
    AssetCreate,
    AssetOut,
    AssetUpdate,
    CSVUploadResult,
    LifecycleEventCreate,
    LifecycleEventOut,
)
from app.services.carbon import calculate_carbon_kg, calculate_circularity_score
from app.services.csv_import import import_assets_from_csv


router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("", response_model=list[AssetOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()


@router.post("", response_model=AssetOut, dependencies=[Depends(require_roles("admin", "manager"))])
def create_asset(asset_in: AssetCreate, db: Session = Depends(get_db)):
    circularity = asset_in.circularity_score
    if circularity == 0 and asset_in.raw_material_kg > 0:
        circularity = calculate_circularity_score(asset_in.raw_material_kg, asset_in.recycled_material_kg)

    asset = Asset(
        id=str(uuid.uuid4()),
        asset_tag=asset_in.asset_tag,
        name=asset_in.name,
        category=AssetCategory(asset_in.category),
        manufacturer=asset_in.manufacturer,
        model=asset_in.model,
        purchase_date=asset_in.purchase_date,
        location=asset_in.location,
        status=LifecycleStatus(asset_in.status),
        usage_hours=asset_in.usage_hours,
        energy_kwh=asset_in.energy_kwh,
        waste_kg=asset_in.waste_kg,
        recycled_material_kg=asset_in.recycled_material_kg,
        raw_material_kg=asset_in.raw_material_kg,
        water_liters=asset_in.water_liters,
        circularity_score=circularity,
        carbon_kg=calculate_carbon_kg(
            asset_in.raw_material_kg,
            asset_in.recycled_material_kg,
            asset_in.energy_kwh,
            asset_in.waste_kg,
            asset_in.water_liters,
        ),
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset


@router.get("/{asset_id}", response_model=AssetOut, dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def get_asset(asset_id: str, db: Session = Depends(get_db)):
    asset = db.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.put("/{asset_id}", response_model=AssetOut, dependencies=[Depends(require_roles("admin", "manager"))])
def update_asset(asset_id: str, asset_in: AssetUpdate, db: Session = Depends(get_db)):
    asset = db.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    data = asset_in.model_dump(exclude_unset=True)
    if "category" in data and data["category"] is not None:
        data["category"] = AssetCategory(data["category"])
    if "status" in data and data["status"] is not None:
        data["status"] = LifecycleStatus(data["status"])
    for key, value in data.items():
        setattr(asset, key, value)
    if asset.circularity_score == 0 and asset.raw_material_kg > 0:
        asset.circularity_score = calculate_circularity_score(asset.raw_material_kg, asset.recycled_material_kg)
    asset.carbon_kg = calculate_carbon_kg(
        asset.raw_material_kg,
        asset.recycled_material_kg,
        asset.energy_kwh,
        asset.waste_kg,
        asset.water_liters,
    )
    asset.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(asset)
    return asset


@router.delete("/{asset_id}", dependencies=[Depends(require_roles("admin"))])
def delete_asset(asset_id: str, db: Session = Depends(get_db)):
    asset = db.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(asset)
    db.commit()
    return {"status": "deleted"}


@router.post("/upload-csv", response_model=CSVUploadResult, dependencies=[Depends(require_roles("admin", "manager"))])
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = file.file.read()
    created, failed, errors = import_assets_from_csv(db, content)
    return CSVUploadResult(created=created, failed=failed, errors=errors)


@router.get("/{asset_id}/lifecycle", response_model=list[LifecycleEventOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_lifecycle(asset_id: str, db: Session = Depends(get_db)):
    return db.query(LifecycleEvent).filter(LifecycleEvent.asset_id == asset_id).all()


@router.post("/{asset_id}/lifecycle", response_model=LifecycleEventOut, dependencies=[Depends(require_roles("admin", "manager"))])
def add_lifecycle_event(asset_id: str, event_in: LifecycleEventCreate, db: Session = Depends(get_db)):
    asset = db.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    event = LifecycleEvent(
        id=str(uuid.uuid4()),
        asset_id=asset_id,
        event_type=LifecycleEventType(event_in.event_type),
        event_date=event_in.event_date or datetime.utcnow(),
        details=event_in.details,
        performed_by=event_in.performed_by,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
