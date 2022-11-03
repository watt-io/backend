from sqlalchemy.orm import Session

from . import models, schemas


def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).first()


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieBase):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie: schemas.MovieBase, movie_id: int):
    db_movie = db.query(models.Movie).filter(
        models.Movie.id == movie_id).first()
    db_movie.title = movie.title
    db_movie.year = movie.year
    db_movie.genre = movie.genre
    db_movie.director = movie.director
    db_movie.synopsis = movie.synopsis
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(
        models.Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
    return db_movie
