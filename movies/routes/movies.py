from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from movies.data.config.connection import DatabaseConnectionHandler
from movies.data.models.movie import MovieModel
from movies.schemas.movie import CreateMovieSchema, MovieSchema

router = APIRouter(prefix='/filmes', tags=['Filmes'])


@router.post('/', response_model=MovieSchema, status_code=HTTPStatus.CREATED)
async def add_new_movie(new_movie: CreateMovieSchema) -> MovieSchema:
    movie_model = MovieModel(**new_movie.model_dump())

    with DatabaseConnectionHandler() as db:
        db.session.add(movie_model)
        db.session.commit()
        db.session.refresh(movie_model)

    return MovieSchema.model_validate(movie_model)


@router.get('/', response_model=list[MovieSchema])
async def get_all_movies() -> list[MovieSchema]:
    with DatabaseConnectionHandler() as db:
        movies = db.session.scalars(select(MovieModel)).all()
        return [MovieSchema.model_validate(movie) for movie in movies]


@router.get('/{movie_id}', response_model=MovieSchema)
async def get_movie_by_id(movie_id: int) -> MovieSchema:
    with DatabaseConnectionHandler() as db:
        movie = db.session.scalar(select(MovieModel).where(MovieModel.id == movie_id))

        if not movie:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Movie not found')

        return MovieSchema.model_validate(movie)
