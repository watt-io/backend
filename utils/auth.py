from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from Services.JwtService import JWTService
from Services.UserService import UserService
from Data.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")  # rota de login

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    # Dependência que extrai o usuário logado do token JWT
    
    payload = JWTService.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    
    user_service = UserService(db)
    user = user_service.user_repo.get_by_id(payload.get("user_id"))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
    return user
