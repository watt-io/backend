from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate



def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        director=movie.director,
        year=movie.year
        

    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Movie).offset(skip).limit(limit).all()



def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
        return db_movie
    return None


def change_movie(db: Session, movie_id: int, movie_update: MovieCreate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        if movie_update.title is not None:
            db_movie.title = movie_update.title
        if movie_update.director is not None:
            db_movie.director = movie_update.director
        if movie_update.year is not None:
            db_movie.year = movie_update.year
        db.commit()
        db.refresh(db_movie)
        return db_movie
    return None     