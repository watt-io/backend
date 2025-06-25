from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.movie import *
from app.crud import movies as crud
from fastapi import HTTPException

router = APIRouter() 

@router.post("/filmes/", response_model=Movie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.get("/filmes/", response_model=list[Movie])
def list_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip, limit)

@router.get("/filmes/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_id(db, movie_id)
    if movie:
        return movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found") 

@router.delete("/filmes/{movie_id}", response_model=Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    return crud.delete_movie(db, movie_id)

@router.put("/filmes/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie:MovieUpdate, db: Session = Depends(get_db)):
    updated = crud.change_movie(db, movie_id, movie)
    if updated:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Movie not found")
