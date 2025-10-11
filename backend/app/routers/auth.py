from fastapi import APIRouter, HTTPException
from .. import db
from ..schemas import UserCreate, Token
from ..core.config import settings
from jose import jwt
from datetime import timedelta, datetime

router = APIRouter(prefix="/auth", tags=["auth"])

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

@router.post("/register")
async def register(user: UserCreate):
    existing = db.get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = db.create_user(user.name, user.email, user.country, user.industry)
    token = create_access_token({"sub": new_user.email})
    return {"status": "success", "user_id": new_user.id, "name": new_user.name, "access_token": token}

@router.post("/login")
async def login(payload: dict):
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email required")
    user = db.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Account not found")
    token = create_access_token({"sub": user.email})
    return {"status": "success", "user_id": user.id, "name": user.name, "access_token": token}
