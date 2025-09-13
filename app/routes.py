from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, database

router = APIRouter()

@router.get("/filmes", response_model=List[schemas.Filme])
def listar_filmes(db: Session = Depends(database.get_db)):
    return crud.get_filmes(db)

@router.get("/filmes/{filme_id}", response_model=schemas.Filme)
def obter_filme(filme_id: int, db: Session = Depends(database.get_db)):
    filme = crud.get_filme(db, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

@router.post("/filmes", response_model=schemas.Filme)
def criar_filme(filme: schemas.FilmeCreate, db: Session = Depends(database.get_db)):
    return crud.criar_filme(db, filme)

@router.put("/filmes/{filme_id}", response_model=schemas.Filme)
def atualizar_filme(filme_id: int, filme: schemas.FilmeUpdate, db: Session = Depends(database.get_db)):
    filme_atualizado = crud.update_filme(db, filme_id, filme)
    if not filme_atualizado:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme_atualizado

@router.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int, db: Session = Depends(database.get_db)):
    filme_deletado = crud.delete_filme(db, filme_id)
    if not filme_deletado:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return {"mensagem": f"Filme com id {filme_id} deletado com sucesso"}
