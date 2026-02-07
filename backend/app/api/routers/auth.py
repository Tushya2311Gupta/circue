from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.models.user import User, UserRole
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
)
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/admin/register", response_model=TokenResponse)
def admin_register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=get_password_hash(payload.password),
        role=UserRole.admin,
    )

    db.add(user)
    db.commit()

    token = create_access_token({"sub": user.email, "role": user.role})

    return TokenResponse(access_token=token, role=user.role)

@router.post("/client/register", response_model=TokenResponse)
def client_register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=get_password_hash(payload.password),
        role=UserRole.client,
    )

    db.add(user)
    db.commit()

    token = create_access_token({"sub": user.email, "role": user.role})

    return TokenResponse(access_token=token, role=user.role)

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email, "role": user.role})

    return TokenResponse(access_token=token, role=user.role)
