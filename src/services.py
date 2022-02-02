from typing import List
import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_movie(db: _orm.Session, id: int):
    movie = db.query(_models.Movies).filter(_models.Movies.id == id).first()
    return movie

async def get_movies(db: _orm.Session) -> List[_schemas.Movie]:
    movies = db.query(_models.Movies).all() 
    return list(map(_schemas.Movie.from_orm, movies))

async def put_movie(db: _orm.Session, movie: _schemas.MovieCreate) -> _schemas.Movie:
    movie = _models.Movies(**movie.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return _schemas.Movie.from_orm(movie)