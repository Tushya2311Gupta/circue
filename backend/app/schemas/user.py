from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str
    is_active: bool = True


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    role: str = "manager"


class UserOut(UserBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
