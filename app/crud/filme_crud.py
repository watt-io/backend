from sqlalchemy.orm import Session
from app.models.filme import Filme
from app.schemas.filme_schema import FilmeCreate

def get_filme(db: Session):
    return db.query(Filme).all()

def get_filme_by_id(db: Session, filme_id: int):
    return db.query(Filme).filter(Filme.id == filme_id).first()

def create_filme(db: Session, filme: FilmeCreate):
    db_filme = Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme