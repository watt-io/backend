from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from app.schemas.movie import MovieRead, MovieCreate, MovieUpdate
from app.repositories.movie import get_all_movies, get_movie, create_movie, delete_movie, update_movie
from app.core.database import get_db

router = APIRouter()

@router.get('/api/v1/movies', response_model=List[MovieRead])
def read_movies(db: Session = Depends(get_db)):
    return get_all_movies(db=db)


@router.get('/api/v1/movies/{movie_id}', response_model=MovieRead)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(db, movie_id)

    if not movie:
        return JSONResponse(status_code = 404, content={"message": "Filme não encontrado"})
    return movie


@router.post('/api/v1/movies', response_model=MovieRead)
def create(db_movie: MovieCreate, db: Session = Depends(get_db)):
    create_movie(db, db_movie)

    return JSONResponse(status_code = 200, content={"message": "Filme cadastrado com sucesso"})


@router.put('/api/v1/movies/{movie_id}', response_model=MovieUpdate)
def update(movie_update: MovieUpdate, movie_id: int, db: Session = Depends(get_db)):
    db_movie = get_movie(db, movie_id)

    if not db_movie:
        return JSONResponse(status_code = 404, content={"message": "Filme não encontrado"})
    
    update_movie(db, movie_id, movie_update)

    return JSONResponse(status_code = 200, content={"message": "Filme atualizado com sucesso"})


@router.delete('/api/v1/movies/{movie_id}')
def delete(movie_id: int, db: Session = Depends(get_db)):
    db_movie = get_movie(db, movie_id)

    if not db_movie:
        return JSONResponse(status_code = 404, content={"message": "Filme não encontrado"})
    
    delete_movie(db, db_movie)

    return JSONResponse(status_code = 200, content={"message": "Filme removido com sucesso"})