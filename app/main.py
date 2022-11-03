from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/filmes/", response_model=schemas.Movie, tags=["filmes"], status_code=201)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie.title)
    if db_movie:
        raise HTTPException(
            status_code=400, detail="Esse filme já foi registrado!")
    return crud.create_movie(db=db, movie=movie)


@app.get("/filmes/", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies


@app.get("/filmes/{filme_id}", response_model=schemas.Movie)
def read_movie(filme_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=filme_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return db_movie


@app.put("/filmes/{filme_id}", response_model=schemas.Movie)
def update_movie(filme_id: int, movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=filme_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return crud.update_movie(db=db, movie=movie, movie_id=filme_id)


@app.delete("/filmes/{filme_id}", response_model=schemas.Movie)
def delete_movie(filme_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=filme_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado!")
    return crud.delete_movie(db=db, movie_id=filme_id)
