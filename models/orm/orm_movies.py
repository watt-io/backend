from sqlalchemy.orm import Session
import uuid
from ..movie_models import Movie
from views.movie_schemas import Movie as movie_schemas

def add_movies(db: Session, movie: movie_schemas):
    uuidOne = str(uuid.uuid1())
    add_movie = Movie(
        id = uuidOne,
        title = movie.title,
        abstract = movie.abstract,
        main_actor = movie.main_actor,
        director = movie.director,
        producion = movie.producion,
        editions = movie.editions,
        streaming = movie.streaming,
        price = movie.price,
        year = movie.year
        
    )
    db.add(add_movie)
    db.commit()
    db.refresh(add_movie)
    return {
        "id": add_movie.id,
        "title": add_movie.title
    }

def get_movies(db: Session, skip: int = 0, limit: int = 20):
    cursor = db.query(Movie).offset(skip).limit(limit).all()
    data = [Movie.getMovies() for Movie in cursor]
    return data

def getbyid_movies(db: Session, id: str):
    data = db.query(Movie).filter(Movie.id == id)
    data = [Movie.getById() for Movie in data]
    return data
