from typing import Generator
from sqlalchemy.orm import Session

# from .datatypes import UpdateStudentValuesType
from models import Filme
from schemas import addFilmeSchema

filmes = Filme


# Get todos filmes
def lista_todos_filmes(db: Session) -> Generator:
    return db.query(filmes).all()

# Get filme especifico
def get_filme(db: Session, id: int):
    return db.query(filmes).filter(
        filmes.id == id
    ).first()


# Post filme no bd
def cria_filme(
    db: Session, filme: addFilmeSchema
):
    novo_filme = Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme
