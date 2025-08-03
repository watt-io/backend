from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.models.usuario import User
from app.schemas.filme import MovieCreate, MovieUpdate, Movie as MovieSchema
from app.middleware.auth_middleware import get_current_user
from app.crud import movie_crud

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=List[MovieSchema])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return movie_crud.get_all(db, skip=skip, limit=limit)


@router.post("/", response_model=MovieSchema)
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return movie_crud.create(db, movie=movie)


@router.get("/{movie_id}", response_model=MovieSchema)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = movie_crud.get(db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    return movie


@router.put("/{movie_id}", response_model=MovieSchema)
def update_movie(
    movie_id: int,
    movie_update: MovieUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_movie = movie_crud.update(db, movie_id=movie_id, movie_update=movie_update)
    if db_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    return db_movie


@router.delete("/{movie_id}")
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    success = movie_crud.delete(db, movie_id=movie_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    return {"message": "Movie removed successfully"}
