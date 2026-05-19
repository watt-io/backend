from fastapi import APIRouter

from src.main.services.movies_service import (
    create_movie_service,
    get_movie_by_id_service,
    list_movies_service,
)
from src.main.validators import (
    MovieCreateResponse,
    MovieCreateValidator,
    MovieDetailResponse,
    MoviesListResponse,
)

movies_router = APIRouter(tags=["Movies"])


@movies_router.post("/movies", response_model=MovieCreateResponse, status_code=201)
async def create_movie_route(body: MovieCreateValidator):
    created_movie = create_movie_service(body)
    return {
        "message": "Movie created successfully",
        "data": created_movie,
    }


@movies_router.get("/movies", response_model=MoviesListResponse)
async def list_movies_route():
    movies = list_movies_service()
    return {
        "total": len(movies),
        "data": movies,
    }


@movies_router.get("/movies/{movie_id}", response_model=MovieDetailResponse)
async def get_movie_by_id_route(movie_id: int):
    movie = get_movie_by_id_service(movie_id)
    return {"data": movie}