import csv
import io
import uuid
from datetime import date

from sqlalchemy.orm import Session

from app.models.asset import Asset, AssetCategory, LifecycleStatus
from app.services.carbon import calculate_carbon_kg, calculate_circularity_score


CSV_FIELDS = [
    "asset_tag",
    "name",
    "category",
    "manufacturer",
    "model",
    "purchase_date",
    "location",
    "status",
    "usage_hours",
    "energy_kwh",
    "waste_kg",
    "recycled_material_kg",
    "raw_material_kg",
    "water_liters",
    "circularity_score",
]


def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def parse_date(value: str | None):
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def import_assets_from_csv(db: Session, content: bytes) -> tuple[int, int, list[str]]:
    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))
    created = 0
    failed = 0
    errors: list[str] = []

    for idx, row in enumerate(reader, start=1):
        try:
            asset_tag = row.get("asset_tag") or f"AUTO-{uuid.uuid4().hex[:8]}"
            circularity_score = parse_float(row.get("circularity_score", "0"))
            raw_material = parse_float(row.get("raw_material_kg", "0"))
            recycled = parse_float(row.get("recycled_material_kg", "0"))
            if circularity_score == 0 and raw_material > 0:
                circularity_score = calculate_circularity_score(raw_material, recycled)

            asset = Asset(
                id=str(uuid.uuid4()),
                asset_tag=asset_tag,
                name=row.get("name", "") or "",
                category=AssetCategory(row.get("category", "laptop")),
                manufacturer=row.get("manufacturer", "") or "",
                model=row.get("model", "") or "",
                purchase_date=parse_date(row.get("purchase_date")),
                location=row.get("location", "") or "",
                status=LifecycleStatus(row.get("status", "purchased")),
                usage_hours=parse_float(row.get("usage_hours", "0")),
                energy_kwh=parse_float(row.get("energy_kwh", "0")),
                waste_kg=parse_float(row.get("waste_kg", "0")),
                recycled_material_kg=recycled,
                raw_material_kg=raw_material,
                water_liters=parse_float(row.get("water_liters", "0")),
                circularity_score=circularity_score,
            )
            asset.carbon_kg = calculate_carbon_kg(
                asset.raw_material_kg,
                asset.recycled_material_kg,
                asset.energy_kwh,
                asset.waste_kg,
                asset.water_liters,
            )
            db.add(asset)
            created += 1
        except Exception as exc:  # pragma: no cover - CSV errors are reported
            failed += 1
            errors.append(f"Row {idx}: {exc}")

    db.commit()
    return created, failed, errors
