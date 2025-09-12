# app/services/jwt_service.py
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

class JWTService:
    @staticmethod
    def create_access_token(data: dict) -> str:
        """
        Gera um token JWT com payload fornecido
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})  # exp define a expiração do token
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str) -> dict:
        """
        Decodifica um token JWT e retorna o payload, ou None se inválido/expirado
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except ExpiredSignatureError:
            print("Token expirado")
            return None
        except JWTError:
            print("Token inválido")
            return None
