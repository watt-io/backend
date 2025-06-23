from http import HTTPStatus

from fastapi import APIRouter

from movies.data.config.connection import DatabaseConnectionHandler
from movies.data.models.movie import MovieModel
from movies.schemas.movie import CreateMovieSchema, MovieSchema

router = APIRouter(prefix='/filmes', tags=['Filmes'])


@router.post('/', response_model=MovieSchema, status_code=HTTPStatus.CREATED)
def add_new_movie(new_movie: CreateMovieSchema) -> MovieSchema:
    movie_model = MovieModel(**new_movie.model_dump())

    with DatabaseConnectionHandler() as db:
        db.session.add(movie_model)
        db.session.commit()
        db.session.refresh(movie_model)

    return MovieSchema.model_validate(movie_model)
