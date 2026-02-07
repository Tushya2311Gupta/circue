import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import assets, auth, predictions, marketplace, partners, esg, circular, reports
from app.core.config import get_settings
from app.core.security import get_password_hash
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.user import User, UserRole


settings = get_settings()
app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(assets.router, prefix=settings.API_V1_STR)
app.include_router(predictions.router, prefix=settings.API_V1_STR)
app.include_router(marketplace.router, prefix=settings.API_V1_STR)
app.include_router(partners.router, prefix=settings.API_V1_STR)
app.include_router(esg.router, prefix=settings.API_V1_STR)
app.include_router(circular.router, prefix=settings.API_V1_STR)
app.include_router(reports.router, prefix=settings.API_V1_STR)


@app.on_event("startup")
def on_startup():
    if settings.AUTO_CREATE_TABLES:
        Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            admin_email = "admin@itam.local"
            admin_password = "ChangeMe123!"
            admin = User(
                id=str(uuid.uuid4()),
                email=admin_email,
                full_name="Platform Admin",
                hashed_password=get_password_hash(admin_password),
                role=UserRole.admin,
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()


@app.get("/health")
def health():
    return {"status": "ok"}
