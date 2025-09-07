from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de CRUD de Filmes",
    description="Desafio tecnico de Roberto Henrique Duarte para um CRUD da Wattio.",
    version="1.0.0"
)

@app.post("/filmes", response_model=schemas.Filme, status_code=201)
def create_filme_endpoint(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    
    return crud.create_filme(db=db, filme=filme)


@app.get("/filmes", response_model=List[schemas.Filme])
def read_filmes_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    filmes = crud.get_filmes(db, skip=skip, limit=limit)
    return filmes


@app.get("/filmes/{filme_id}", response_model=schemas.Filme)
def read_filme_endpoint(filme_id: int, db: Session = Depends(get_db)):
    
    db_filme = crud.get_filme(db, filme_id=filme_id)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return db_filme

@app.get("/")
def read_root():
    """ verificar se a API está online."""
    return {"message": "Bem-vindo a API de Filmes da Wattio🤖. Espero que gostem e possamos fazer parte da mesma equipe em breve! Acesse /docs para ver a documentação."}