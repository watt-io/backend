from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/filmes/")
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    
    res = crud.RepositorioFilmes(db).consultar(movie.title)
    if res:
        raise HTTPException(status_code=400, detail="Filme ja registrado")
    new_movie = crud.RepositorioFilmes(db).inserir(movie)
    return new_movie

@app.get("/filmes/")
def show_movies(db: Session = Depends(get_db)):
    return crud.RepositorioFilmes(db).exibir()

@app.get("/filmes/{id}")
def search_movie(id: str,  db: Session = Depends(get_db)):
    filme = crud.RepositorioFilmes(db).consultar(id)
    if filme is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return filme