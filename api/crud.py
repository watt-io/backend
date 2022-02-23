from typing import Generator
from sqlalchemy.orm import Session

from .models import Movie
from .schemas import CreateMovieSchema

movies = Movie


def create_movie(db: Session, movie: CreateMovieSchema):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


def retrieve_all_movies(db: Session) -> Generator:
    return db.query(movies).all()


def retrieve_movie(db: Session, movie_id: int):
    return db.query(movies).filter(movies.id == movie_id).first()
