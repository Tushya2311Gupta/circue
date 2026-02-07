# API Design (REST)

Base URL: `/api/v1`

## Auth
- `POST /auth/login`
  - Body: form fields `username`, `password`
  - Response: `{ "access_token": "...", "token_type": "bearer" }`
- `POST /auth/register` (Admin only)
  - Body: `{ "email": "", "full_name": "", "password": "", "role": "admin|manager|auditor" }`

## Assets
- `GET /assets`
- `POST /assets`
  - Body: `AssetCreate` (see backend schemas)
- `GET /assets/{id}`
- `PUT /assets/{id}`
- `DELETE /assets/{id}`
- `POST /assets/upload-csv`
  - Body: `multipart/form-data` with `file`
- `GET /assets/{id}/lifecycle`
- `POST /assets/{id}/lifecycle`
  - Body: `{ "event_type": "purchase|use|repair|reuse|refurbish|recycle|retire|donate", "details": "", "performed_by": "" }`

## AI Optimization
- `POST /ai/predict`
- `POST /ai/predict/{asset_id}`
  - Body:
```json
{
  "raw_material_kg": 20,
  "recycled_material_kg": 5,
  "waste_kg": 2,
  "energy_kwh": 120,
  "water_liters": 140,
  "machine_downtime_min": 45,
  "production_volume_units": 80,
  "material_recovery_rate": 0.6,
  "circularity_score": 62
}
```

## Marketplace
- `GET /marketplace/listings`
- `POST /marketplace/listings`
- `PUT /marketplace/listings/{id}`

## Partners
- `GET /partners`
- `POST /partners`
- `PUT /partners/{id}`

## Circular Economy
- `GET /circular/donations`
- `POST /circular/donations`
- `GET /circular/recycling`
- `POST /circular/recycling`

## ESG
- `GET /esg/metrics`
- `POST /esg/metrics`
- `GET /esg/snapshot?period_start=YYYY-MM-DD&period_end=YYYY-MM-DD`

## Reports
- `GET /reports/esg?period_start=YYYY-MM-DD&period_end=YYYY-MM-DD&format=csv|pdf`
