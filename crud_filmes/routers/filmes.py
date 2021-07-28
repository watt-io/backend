from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()
get_db = database.get_db

@router.get('/filmes', response_model=List[schemas.ShowFilme],tags=['Filme'])
def get_all_movies(db: Session = Depends(get_db)):
    films = db.query(models.Filme).all()
    return films

@router.post('/filmes',  status_code=status.HTTP_201_CREATED,
            response_model=schemas.ShowFilme, tags=['Filme'])
def insert_movie(request: schemas.Filme, db: Session = Depends(get_db)):
    new_film = models.Filme(
        nome=request.nome, 
        ano=request.ano, 
        categoria=request.categoria,
        user_id=1
        )
    db.add(new_film)
    db.commit()
    db.refresh(new_film)

    return new_film

@router.get('/filmes/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowFilme, tags=['Filme'])
def get_a_movie(id:int, db: Session = Depends(get_db)):
    film_id = db.query(models.Filme).filter(models.Filme.id == id).first()
    if not film_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    return film_id

@router.delete('/filmes/{id}', status_code=status.HTTP_204_NO_CONTENT,
                tags=['Filme'])
def delete_movie(id: int, db: Session = Depends(get_db)):
    filme_del = db.query(models.Filme).filter(models.Filme.id == id)
    if not filme_del.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    filme_del.delete(synchronize_session=False)
    db.commit()
    return {'detail':'Done'}