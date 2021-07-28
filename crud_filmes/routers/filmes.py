from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import filmes

router = APIRouter(
    prefix="/filmes",
    tags=["Filmes"]
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowAllFilme])
def get_all_movies(db: Session = Depends(get_db)):
    return filmes.get_all(db)

@router.post('/',  status_code=status.HTTP_201_CREATED,
            response_model=schemas.ShowFilme)
def insert_movie(request: schemas.Filme, db: Session = Depends(get_db)):
    return filmes.insert(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowFilme)
def get_a_movie(id:int, db: Session = Depends(get_db)):
    return filmes.get(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(id: int, db: Session = Depends(get_db)):
    return filmes.delete(id, db)