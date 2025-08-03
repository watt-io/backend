from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate

def get_movies(db: Session, skip: int = 0, limit: int = 10) -> List[Movie]:
    return db.query(Movie).offset(skip).limit(limit).all()


def get_movie(db: Session, movie_id: int) -> Optional[Movie]:
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_movies_by_title(db: Session, title: str) -> List[Movie]:
    return db.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()


def create_movie(db: Session, movie: MovieCreate) -> Movie:
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie_id: int, movie: MovieUpdate) -> Optional[Movie]:
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        return None
    for key, value in movie.dict(exclude_unset=True).items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int) -> Optional[Movie]:
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        return None
    db.delete(db_movie)
    db.commit()
    return db_movie
