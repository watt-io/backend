# app/services/user_service.py
from sqlalchemy.orm import Session
from Models.UserModel import User
from DTOs.UserDTOs import UserCreate
from Services.HashService import HashService
from Services.JwtService import JWTService
from Repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, user_create: UserCreate) -> User:
 
        hashed_password = HashService.hash_password(user_create.password)
        user = User(
            username=user_create.username,
            email=user_create.email,
            hashed_password=hashed_password,
            is_active=user_create.is_active
        )
        return self.user_repo.create(user)
    
    def authenticate(self, email: str, password: str) -> str | None:
        
        user = self.user_repo.get_by_email(email)
        if not user or not HashService.verify_password(password, user.hashed_password):
            return None
        # Retorna token JWT com ID e username como payload
        token = JWTService.create_access_token({"user_id": user.id, "username": user.username})
        return token
