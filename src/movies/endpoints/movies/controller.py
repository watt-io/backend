from fastapi import APIRouter, Depends, HTTPException, status, Request, FastAPI
from dependency_injector.wiring import inject, Provide

from movies.endpoints.movies.schema import MovieSchema, MoviesSchema, UpdateMovieSchema
from movies.endpoints.movies.service import MoviesService
from movies.infrastructure.containers import Container

router = APIRouter()


@router.post("/movies", status_code=status.HTTP_201_CREATED)
@inject
async def create_movies(request: Request, register_movie: MovieSchema,
                        movies_service: MoviesService = Depends(Provide[Container.movies_services])):
    return await movies_service.create_movie(register_movie.dict())


@router.get("/movies/{movie_id}", status_code=status.HTTP_200_OK, response_model=MoviesSchema)
@inject
async def get_by_id(request: Request, movie_id: int,
                    movies_service: MoviesService = Depends(Provide[Container.movies_services])):
    return await movies_service.get_movie_by_id(movie_id=movie_id)



def configure(app: FastAPI):
    app.include_router(router)
