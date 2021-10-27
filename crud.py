from sqlalchemy.orm import Session
import models, schemas

def cria_filme(db: Session, filme: schemas.Filme):
    db_filme = models.Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def get_filme_by_id(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first() #retorna um Filme 

def get_filmes(db: Session):
    return db.query(models.Filme).all() #retorna o db de filmes