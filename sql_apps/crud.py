from sqlalchemy.orm import Session
from sql_apps.models import MovieDb
from sql_apps.schemas import Movie
from uuid import uuid4 as uuid

movie_db = MovieDb


def create_movie(movie: Movie, db: Session):
    if movie.id == "string":
        movie.id = str(uuid())
    new_movie = MovieDb(**movie.dict())
    if not retrieve_movie(new_movie.id, db):
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    return None


def retrieve_all_movies(db: Session):
    return db.query(movie_db).all()


def retrieve_movie(movie_id: str, db: Session):
    return db.query(movie_db).filter(movie_db.id == movie_id).one_or_none()


def remove_movie(movie_id: str, db: Session):
    if movie := retrieve_movie(movie_id, db):
        db.delete(movie)
        db.commit()
        return movie
    return None


def update_movie(movie_id: str, db: Session, updated_movie: Movie):
    if movie := retrieve_movie(movie_id, db):
        for item, value in vars(updated_movie).items():
            setattr(movie, item, value) if value else None
        db.commit()
        db.refresh(movie)
        return movie
    return None
