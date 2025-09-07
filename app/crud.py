from sqlalchemy.orm import Session
from . import models, schemas

def get_filme(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first()

def get_filmes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Filme).offset(skip).limit(limit).all()

def create_filme(db: Session, filme: schemas.FilmeCreate):
    db_filme = models.Filme(
        titulo=filme.titulo,
        diretor=filme.diretor,
        ano=filme.ano
    )
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme