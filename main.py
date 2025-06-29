from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas

# Cria as tabelas no banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET 
@app.get("/filmes", response_model=List[schemas.Filme])
def listar_filmes(db: Session = Depends(get_db)):
    
    return db.query(models.FilmeModel).all()

@app.get("/filmes/{id}", response_model=schemas.Filme)
def obter_filme(id: int, db: Session = Depends(get_db)):

    filme = db.query(models.FilmeModel).filter(models.FilmeModel.id == id).first()

    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    return filme

# POST

@app.post("/filmes", response_model=schemas.Filme)
def criar_filme(filme: schemas.Filme, db: Session = Depends(get_db)):

    novo_filme = models.FilmeModel(**filme.model_dump())

    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)

    return novo_filme

# DELETE

@app.delete("/filmes/{id}")
def deletar_filme(id: int, db: Session = Depends(get_db)):

    filme = db.query(models.FilmeModel).filter(models.FilmeModel.id == id).first()

    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    db.delete(filme)
    db.commit()

    return filme