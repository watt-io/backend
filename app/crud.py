from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, database, models

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

def criar_filme(db: Session, filme: schemas.FilmeCreate):
    novo_filme = models.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

def get_filmes(db: Session):
    return db.query(models.Filme).all()

def get_filme(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id == filme_id).first()

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
