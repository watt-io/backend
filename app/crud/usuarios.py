from sqlalchemy.orm import Session
from typing import Optional
from app.models.usuario import User
from app.schemas.usuario import UserCreate, UserUpdate
from app.auth.jwt_handler import get_password_hash, verify_password


class CRUDUser:

    def get(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, password_hash=hashed_password, name=user.name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    def update(
        self, db: Session, user_id: int, user_update: UserUpdate
    ) -> Optional[User]:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            update_data = user_update.dict(exclude_unset=True)

            if "password" in update_data:
                update_data["password_hash"] = get_password_hash(
                    update_data.pop("password")
                )

            for field, value in update_data.items():
                if hasattr(db_user, field):
                    setattr(db_user, field, value)

            db.commit()
            db.refresh(db_user)
        return db_user

    def delete(self, db: Session, user_id: int) -> bool:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False


user_crud = CRUDUser()
