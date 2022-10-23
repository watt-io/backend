from sqlalchemy.orm import Session

from . import models, schemas


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(name=movie.name, description=movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
