from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_all_movies(db: Session):
    return db.query(Movie).all()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(name = movie.name, description = movie.description, genre = movie.genre)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    
    return db_movie


def update_movie(db: Session, movie_id: int, movie_update: MovieUpdate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
        
    for field, value in movie_update.model_dump(exclude_unset=True).items():
        setattr(db_movie, field, value)

    db.commit()
    db.refresh(db_movie)


def delete_movie(db: Session, movie: Movie):
    db.delete(movie)
    db.commit()