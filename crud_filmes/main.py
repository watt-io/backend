from fastapi import FastAPI, Depends
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

@app.post('/filmes')
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