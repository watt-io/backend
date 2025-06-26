
from sqlalchemy.orm import Session
from app import tabelas, dados

def buscar_todos(db: Session):
    return db.query(tabelas.Filme).all()

def buscar_por_id(db: Session, filme_id: int):
    return db.query(tabelas.Filme).filter(tabelas.Filme.id == filme_id).first()

def criar(db: Session, filme: dados.FilmeCreate):
    novo_filme = tabelas.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

def remover(db: Session, filme_id: int):
    filme = buscar_por_id(db, filme_id)
    if filme:
        db.delete(filme)
        db.commit()
        return True
    return False

def atualizar(db: Session, filme_id: int, dados_filme: dados.FilmeCreate):
    filme = buscar_por_id(db, filme_id)
    if filme:
        for campo, valor in dados_filme.dict().items():
            setattr(filme, campo, valor)
        db.commit()
        db.refresh(filme)
        return filme
    return None
