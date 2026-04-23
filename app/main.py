from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Filmes 🎬")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/filmes", response_model=list[schemas.FilmeResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_filmes(db)

@app.post("/filmes", response_model=schemas.FilmeResponse)
def criar(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    return crud.criar_filme(db, filme)

@app.get("/filmes/{id}", response_model=schemas.FilmeResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    filme = crud.buscar_filme(db, id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme