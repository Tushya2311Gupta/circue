# Sustainable IT Asset Management Platform for Net Zero using Circular Economy

Enterprise-grade platform to track IT assets across the full lifecycle, quantify Scope-3 impact, and optimize reuse/refurbish/recycle decisions with AI-driven waste risk predictions.

## Architecture Summary
- **Frontend:** React (Vite) enterprise UI with dashboards, charts, and AI prediction workflows.
- **Backend:** FastAPI REST API with JWT auth and role-based access (Admin, Manager, Auditor).
- **ML Inference:** Random Forest classifier (scikit-learn) for high-waste risk prediction.
- **Database:** PostgreSQL with asset, lifecycle, ESG, prediction, marketplace, and partner records.
- **Deployment:** Dockerized services compatible with AWS/GCP/Azure.

Mermaid diagram: `docs/architecture.mmd`

## Security Considerations
- JWT-based authentication with role-based authorization.
- Audit trail: lifecycle events + prediction logs.
- Principle of least privilege for Admin/Manager/Auditor roles.
- Transport security via HTTPS termination (cloud LB or API gateway).
- Secrets managed via environment variables or secret manager.

## Key Features
- **Asset onboarding:** manual CRUD + CSV upload.
- **Lifecycle tracking:** purchase → use → repair → reuse → refurbish → recycle.
- **Carbon analytics:** asset-level carbon and circularity score.
- **AI optimization:** Random Forest high-waste risk prediction + recommended action.
- **Circular economy workflows:** reuse marketplace, partner directory, donation & recycling tracking.
- **ESG reporting:** Scope-3 dashboard + SDG-12/SDG-17 indicators; PDF/CSV export.

## Local Development

### Backend
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker (recommended)
```bash
docker-compose up --build
```

## Default Admin
On first boot, a default Admin is created:
- **Email:** `admin@itam.local`
- **Password:** `ChangeMe123!`

Update in production and rotate secrets.

## ML Model Training
```bash
python backend/scripts/train_model.py \
  --input dataset/circular_economy_dataset.csv \
  --output backend/models/waste_risk_rf.pkl \
  --version rf-v1
```

Model loaded at runtime from `backend/models/waste_risk_rf.pkl` via `MODEL_PATH`.

## API & Schema References
- API: `docs/api.md`
- DB schema: `docs/db-schema.sql`

## Frontend Routes
- `/` Executive Dashboard
- `/assets` Asset Registry
- `/assets/:assetId` Asset Detail
- `/ai` AI Optimization
- `/circular` Circular Workflows
- `/marketplace` Internal Reuse Marketplace
- `/partners` Refurbisher & Recycler Directory
- `/reports` ESG & Net Zero Reporting

## Deployment Strategy
- Dockerized services deployed to ECS/EKS/AKS/GKE.
- PostgreSQL managed service (RDS/Cloud SQL/Azure DB).
- API behind WAF + TLS termination; frontend on CDN.
- Observability: metrics + distributed tracing.

## Scalability Roadmap
- Add event-driven ingestion for IoT energy data (Kafka/PubSub).
- Automated asset classification and anomaly detection.
- Advanced scenario planning for Net Zero pathways.
- Multi-tenant SaaS readiness with tenant isolation.
- Model monitoring & drift detection pipeline.
