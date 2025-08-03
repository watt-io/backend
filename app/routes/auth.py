from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database.connection import get_db
from app.models.usuario import User
from app.schemas.usuario import UserCreate, UserLogin, User as UserSchema
from app.schemas.token import Token
from app.auth.jwt_handler import (
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.middleware.auth_middleware import get_current_user
from app.crud import user_crud

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=UserSchema)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    return user_crud.create(db, user=user)


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.authenticate(db, email=user.email, password=user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserSchema)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user
