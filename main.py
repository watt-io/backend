from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models import Base, Filme, FilmeCreate, FilmeRead
from database import engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD de Filmes")

@app.get("/filmes", response_model=List[FilmeRead])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(Filme).all()

@app.post("/filmes", response_model=FilmeRead)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    db_filme = Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

@app.get("/filmes/{id}", response_model=FilmeRead)
def buscar_filme(id: int, db: Session = Depends(get_db)):
    filme = db.query(Filme).filter(Filme.id == id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme
