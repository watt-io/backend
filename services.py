from typing import TYPE_CHECKING, List
import database as _db
import models as _models
import schemas as _schemas
import sqlalchemy.orm as _orm

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_movie(
    movie: _schemas.CreateMovie,
    db: _orm.Session,
) -> _schemas.Movie:
    movie = _models.Movies(**movie.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return _schemas.Movie.from_orm(movie)


async def get_all_movies(db: _orm.Session) -> List[_schemas.Movie]:
    movies = db.query(_models.Movies).all()
    return list(map(_schemas.Movie.from_orm, movies))


async def get_movie(id: int, db: _orm.Session):
    movie = db.query(_models.Movies).filter(_models.Movies.id == id).first()
    return movie
