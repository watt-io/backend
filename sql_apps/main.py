from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sql_apps.database import SessionLocal, engine
from starlette.responses import RedirectResponse
from sql_apps import models, schemas
from sql_apps.crud import (
    create_movie,
    remove_movie,
    retrieve_all_movies,
    retrieve_movie,
    update_movie,
)

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota raiz
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


# Rota get todos os filmes
@app.get("/filmes")
def get_all_movies(db: Session = Depends(get_db)):
    if movies := retrieve_all_movies(db):
        return movies
    raise HTTPException(status_code=404, detail="Movies not found")


# Rota get filme especifico
@app.get("/filmes/{filme_id}")
def get_movie(movie_id: str, db: Session = Depends(get_db)):
    if movie := retrieve_movie(movie_id, db):
        return movie
    raise HTTPException(status_code=404, detail="Movie not found")


# Rota inserir
@app.post("/filmes")
def post_movie(movie: schemas.Movie, db: Session = Depends(get_db)):
    if movie := create_movie(movie, db):
        return {"Message": f"Movie {movie} added"}
    raise HTTPException(status_code=404, detail="Movie not added")


# Rota deletar
@app.delete("/filmes/{filme_id}")
def delete_movie(movie_id: str, db: Session = Depends(get_db)):
    if movie := remove_movie(movie_id, db):
        return {"Message": f"Movie {movie} removed"}
    raise HTTPException(status_code=404, detail="Movie not removed")


# Rota atualizar
@app.put("/filmes/{filme_id}")
def put_movie(movie_id: str, new_movie: schemas.Movie, db: Session = Depends(get_db)):
    if movie := update_movie(movie_id, db, new_movie):
        return {"Message": f"Movie {movie} updated"}
    raise HTTPException(status_code=404, detail="Movie not updated")
