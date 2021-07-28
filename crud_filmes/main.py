from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash

app = FastAPI() 

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/filmes', tags=['Filme'])
def get_all_movies(db: Session = Depends(get_db)):
    films = db.query(models.Filme).all()
    return films

@app.post('/filmes',  status_code=status.HTTP_201_CREATED,
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

@app.get('/filmes/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowFilme, tags=['Filme'])
def get_a_movie(id:int, db: Session = Depends(get_db)):
    film_id = db.query(models.Filme).filter(models.Filme.id == id).first()
    if not film_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    return film_id

@app.delete('/filmes/{id}', status_code=status.HTTP_204_NO_CONTENT,
                tags=['Filme'])
def delete_movie(id: int, db: Session = Depends(get_db)):
    filme_del = db.query(models.Filme).filter(models.Filme.id == id)
    if not filme_del.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    filme_del.delete(synchronize_session=False)
    db.commit()
    return {'detail':'Done'}
    


@app.post('/user', response_model=schemas.ShowUser, tags=['User'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, password=Hash.bcrypt(
        request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User com id {id} indisponível!")
    return user