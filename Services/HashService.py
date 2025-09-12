# app/services/hash_service.py
from passlib.context import CryptContext

# CryptContext facilita o hashing seguro de senhas usando algoritmos como bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashService:
    @staticmethod
    def hash_password(password: str) -> str:

        # Recebe uma senha em texto puro e retorna a senha hash

        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        # Verifica se a senha em texto puro corresponde ao hash armazenado
        return pwd_context.verify(password, hashed_password)
