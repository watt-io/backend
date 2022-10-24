from unittest.util import strclass
from fastapi import FastAPI, HTTPException, status, Depends
from typing import Union
from uuid import UUID, uuid4
from . import models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session

from app.schemas import Movie

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/filmes")
def get_filmes(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@app.post("/filmes")
def post_filmes(filme: Movie, db: Session = Depends(get_db)):
    
    movie_model = models.Movie()
    movie_model.title = filme.title
    movie_model.director = filme.director
    movie_model.duration = filme.duration
    movie_model.release_year = filme.release_year
    movie_model.country_of_origin = filme.country_of_origin
    movie_model.overview = filme.overview
    movie_model.budget = filme.budget
    movie_model.rating = filme.rating
    movie_model.genre = filme.genre
    movie_model.starring = filme.starring

    db.add(movie_model)
    db.commit()

    return filme

@app.get("/filmes/{movie_id}")
def get_filmes_id(movie_id: str, db: Session = Depends(get_db)):
    movie_model = db.query(models.Movie).filter(models.Movie.id == movie_id).first()

    if movie_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {movie_id} : Does not Exist"
        )

    return movie_model

    