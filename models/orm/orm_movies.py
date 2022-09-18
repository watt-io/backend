from sqlalchemy.orm import Session
import uuid
from ..movie_models import Movie
from views.movie_schemas import Movie as movie_schemas

def add_movies(db: Session, movie: movie_schemas):
    uuidOne = str(uuid.uuid4())
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

def delete(db: Session, id: str):
    movie = db.query(Movie).filter(Movie.id == id).one()
    db.delete(movie)
    db.commit()
    msg = "Deleted success."
    return msg

def update(db: Session, id: str(uuid.uuid1), movie: movie_schemas):
    data = db.query(Movie).filter(Movie.id == id).one()
    
    data.title = movie.title
    data.abstract = movie.abstract
    data.main_actor = movie.main_actor
    data.director = movie.director
    data.producion = movie.producion
    data.editions = movie.editions
    data.streaming = movie.streaming
    data.price = movie.price
    data.year = movie.year
        

    db.merge(data)
    db.commit()
    msg = "Update movies success."
    return msg