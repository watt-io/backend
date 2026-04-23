from sqlalchemy.orm import Session
from . import models, schemas

def criar_filme(db: Session, filme: schemas.FilmeCreate):
    novo_filme = models.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

def listar_filmes(db: Session):
    return db.query(models.Filme).all()

def buscar_filme(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first()