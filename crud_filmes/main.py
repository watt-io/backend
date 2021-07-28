from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI() 

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/filmes')
def get_all_movies(db: Session = Depends(get_db)):
    films = db.query(models.Filme).all()
    return films

@app.post('/filmes',  status_code=status.HTTP_201_CREATED, response_model=schemas.ShowFilme)
def insert_movie(request: schemas.Filme, db: Session = Depends(get_db)):
    new_film = models.Filme(
        nome=request.nome, 
        ano=request.ano, 
        categoria=request.categoria
        )
    db.add(new_film)
    db.commit()
    db.refresh(new_film)

    return new_film

@app.get('/filmes/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowFilme)
def get_a_movie(id:int, db: Session = Depends(get_db)):
    film_id = db.query(models.Filme).filter(models.Filme.id == id).first()
    if not film_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    return film_id

@app.delete('/filmes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(id: int, db: Session = Depends(get_db)):
    filme_del = db.query(models.Filme).filter(models.Filme.id == id)
    if not filme_del.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    filme_del.delete(synchronize_session=False)
    db.commit()
    return {'detail':'Done'}
    
@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
