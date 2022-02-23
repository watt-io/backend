from typing import Generator
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .crud import create_movie, retrieve_all_movies, retrieve_movie
from .database import Base, SessionLocal, engine
from .datatypes import MovieType
from .schemas import CreateMovieSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies/", status_code=status.HTTP_200_OK)
def get_all_movies(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_movies(db):
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There're no registered movies.")


@app.post("/movies/", status_code=status.HTTP_201_CREATED)
def post_movie(movie: CreateMovieSchema, db: Session = Depends(get_db)) -> MovieType:
    if result := create_movie(db, movie):
        return result
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/movies/{movies_id}/", status_code=status.HTTP_200_OK)
def get_movie(movie_id: int, db: Session = Depends(get_db)) -> MovieType:
    if result := retrieve_movie(db, movie_id):
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie {movie_id} wasn't found")
