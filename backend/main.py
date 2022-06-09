
from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import crud
import models.model as model
import schemas.schema as schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Desafio Watt  ",
    description="API REST com Fast Api e persistência Sqlite3 - Robinson Enedino",
    version="1.0.0",
    contact={
    "name": "Robinson Enedino",
    "url": "https://www.enedino.com.br/portfolio/",
    "email": "robinsonbrz@gmail.com",
    },
)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Root path - Interface Front End
@app.get("/", response_class=HTMLResponse)
def root(request:Request , db: Session = Depends(get_db)):
    filmes = crud.get_movies(db=db, skip=0, limit=1000)
    context = {'request': request, "filmes":filmes}
    return templates.TemplateResponse("index.html", context)


@app.get('/filmes', response_model=List[schema.Movie])
def recupera_todos_filmes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db=db, skip=skip, limit=limit)
    return movies


@app.get('/filmes/{id}', response_model=schema.Movie)
def recupera_filme_por_id(id: str, db: Session = Depends(get_db)):
    movies = crud.get_movie_by_movie_id(db=db, id=id)
    return movies


@app.post('/add_filme', response_model=schema.MovieAdd)
def adiciona_filme(movie: schema.MovieAdd, db: Session = Depends(get_db)):
    return crud.add_movie_details_to_db(db=db, movie=movie)


@app.delete('/delete_filme/{id}')
def deleta_filme_por_id(id: int, db: Session = Depends(get_db)):
    details = crud.get_movie_by_movie_id(db=db, id=id)
    if not details:
        raise HTTPException(status_code=404, detail="No record found to delete")

    try:
        crud.delete_movie_details_by_id(db=db, id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_filme', response_model=schema.Movie)
def update_filmes(id: int, update_param: schema.UpdateMovie, db: Session = Depends(get_db)):
    details = crud.get_movie_by_movie_id(db=db, id=id)
    if not details:
        raise HTTPException(status_code=404, detail="No record found to update")

    return crud.update_movie_details(db=db, details=update_param, id=id)


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')

