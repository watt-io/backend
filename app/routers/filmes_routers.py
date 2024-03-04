from fastapi import APIRouter, HTTPException
from app.db.database import *
from app.model.filmes_model import *

# Configurando a rota filmes
router = APIRouter(prefix="/filmes")

# Rota para listar todos os filmes
@router.get("")
def listar_filmes():
    db = SessionLocal()
    filmes = db.query(Filme).all()
    return filmes


# Rota para listar filme por id
@router.get("/{filme_id}")
def listar_filme_por_id(filme_id: int):
    db = SessionLocal()
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return filme


# Rota para cadastrar um novo filme
@router.post("")
def cadastrar_filme(filme: FilmeCreate):
    db = SessionLocal()
    db_filme = Filme(**filme.model_dump())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme
