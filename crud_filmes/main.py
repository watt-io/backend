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

@app.post('/filmes',  status_code=status.HTTP_201_CREATED)
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

@app.get('/filmes/{id}', status_code=status.HTTP_200_OK)
def get_a_movie(id:int, response: Response, db: Session = Depends(get_db)):
    film_id = db.query(models.Filme).filter(models.Filme.id == id).first()
    if not film_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Filme com id {id} indisponível!")

    return film_id
