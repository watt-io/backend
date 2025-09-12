# app/controllers/user_controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from DTOs.UserDTOs import UserCreate, UserResponse
from Services.UserService import UserService
from Data.session import get_db
from fastapi.security import OAuth2PasswordRequestForm

router_user = APIRouter(prefix="/users", tags=["Users"])

@router_user.post("/", response_model=UserResponse)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
   
    service = UserService(db)
    # Checa se usuário ou e-mail já existem
    if service.user_repo.get_by_email(user_create.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado")
    if service.user_repo.get_by_username(user_create.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username já cadastrado")
    user = service.create_user(user_create)
    return user

@router_user.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login usando OAuth2PasswordRequestForm
    """
    service = UserService(db)
    token = service.authenticate(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"access_token": token, "token_type": "bearer"}