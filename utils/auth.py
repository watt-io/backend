# dependencies/auth_token.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Services.JwtService import JWTService
from sqlalchemy.orm import Session
from Data.session import get_db
from Services.UserService import UserService

# Cria um esquema que espera "Authorization: Bearer <token>"
bearer_scheme = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(get_db)):
    """
    Extrai o usuário do token JWT enviado no header Authorization
    """
    payload = JWTService.decode_access_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    
    user_service = UserService(db)
    user = user_service.user_repo.get_by_id(payload.get("user_id"))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
    
    return user
