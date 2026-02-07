from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.models.recycling import RecyclingRecord
from app.models.donation import DonationRecord


def calculate_esg_snapshot(db: Session, period_start: date, period_end: date) -> dict[str, float]:
    assets = (
        db.query(
            func.sum(Asset.carbon_kg),
            func.avg(Asset.circularity_score),
            func.sum(Asset.waste_kg),
            func.sum(Asset.recycled_material_kg),
        )
        .all()
    )
    scope3 = float(assets[0][0] or 0)
    circularity = float(assets[0][1] or 0)
    waste = float(assets[0][2] or 0)
    recycled = float(assets[0][3] or 0)

    recycling_count = db.query(func.count(RecyclingRecord.id)).scalar() or 0
    donation_count = db.query(func.count(DonationRecord.id)).scalar() or 0

    sdg12 = min(1.0, (recycled / (waste + 1e-6)) / 2)
    sdg17 = min(1.0, (recycling_count + donation_count) / 10)

    return {
        "scope3_emissions_kg": round(scope3, 2),
        "circularity_index": round(circularity, 2),
        "waste_diverted_kg": round(recycled, 2),
        "recycled_materials_kg": round(recycled, 2),
        "sdg12_alignment": round(sdg12, 2),
        "sdg17_alignment": round(sdg17, 2),
    }
