import json
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.models.asset import Asset
from app.models.prediction import PredictionLog
from app.schemas.prediction import PredictionInput, PredictionLogOut, PredictionResponse
from app.services.ml import predict_waste_risk


router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/predict", response_model=PredictionResponse, dependencies=[Depends(require_roles("admin", "manager"))])
def predict(payload: PredictionInput, db: Session = Depends(get_db)):
    features = payload.model_dump()
    result = predict_waste_risk(features)

    log = PredictionLog(
        id=str(uuid.uuid4()),
        asset_id=None,
        input_features=json.dumps(features),
        risk_level=result.risk_level,
        confidence=result.confidence,
        recommended_action=result.recommended_action,
        model_version=result.model_version,
    )
    db.add(log)
    db.commit()
    return result.__dict__


@router.post("/predict/{asset_id}", response_model=PredictionResponse, dependencies=[Depends(require_roles("admin", "manager"))])
def predict_for_asset(asset_id: str, payload: PredictionInput, db: Session = Depends(get_db)):
    asset = db.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    features = payload.model_dump()
    result = predict_waste_risk(features)

    log = PredictionLog(
        id=str(uuid.uuid4()),
        asset_id=asset_id,
        input_features=json.dumps(features),
        risk_level=result.risk_level,
        confidence=result.confidence,
        recommended_action=result.recommended_action,
        model_version=result.model_version,
    )
    db.add(log)
    db.commit()
    return result.__dict__


@router.get("/logs", response_model=list[PredictionLogOut], dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def list_logs(db: Session = Depends(get_db)):
    return db.query(PredictionLog).order_by(PredictionLog.created_at.desc()).all()
