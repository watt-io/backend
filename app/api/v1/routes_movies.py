from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.movie import Movie, MovieCreate, MovieUpdate
from app.crud.movie import (
    get_movies,
    get_movie,
    get_movies_by_title,
    create_movie,
    update_movie,
    delete_movie,
)
from app.db.session import get_db

router = APIRouter()

# Define the API routes for listing movies
@router.get(
    "/",
    response_model=List[Movie],
    summary="List movies",
    description="Returns a list of all registered movies."
)
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_movies(db, skip=skip, limit=limit)


@router.get(
    "/{movie_id}",
    response_model=Movie,
    summary="Get movie by ID",
    description="Returns a specific movie by its ID."
)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.get(
    "/title/{title}",
    response_model=List[Movie],
    summary="Get movies by title",
    description="Returns a list of movies that match the given title."
)
def read_movies_by_title(title: str, db: Session = Depends(get_db)):
    return get_movies_by_title(db, title)


@router.post(
    "/",
    response_model=Movie,
    status_code=201,
    summary="Create new movie",
    description="Adds a new movie."
)
def create_new_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db, movie)


@router.put(
    "/{movie_id}",
    response_model=Movie,
    summary="Update movie",
    description="Updates an existing movie by its ID."
)
def update_existing_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    db_movie = update_movie(db, movie_id, movie)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.delete(
    "/{movie_id}",
    response_model=Movie,
    summary="Delete movie",
    description="Removes a movie by its ID."
)
def delete_existing_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = delete_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie
