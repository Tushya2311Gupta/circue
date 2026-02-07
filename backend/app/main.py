from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.user import User, UserRole
from app.core.security import get_password_hash

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.AUTO_CREATE_TABLES:
        Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            admin = User(
                email="admin@itam.local",
                full_name="Platform Admin",
                hashed_password=get_password_hash("ChangeMe123!"),
                role=UserRole.admin,
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()

    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN, "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)