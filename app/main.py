# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.database import Base, engine, SessionLocal
from app.models import Movie

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class MovieSchema(BaseModel):
    title: str
    director: str
    year: int


@app.post("/movies/")
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
    new_movie = Movie(title=movie.title, director=movie.director, year=movie.year)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


@app.get("/movieslist/")
def read_movies_list(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
