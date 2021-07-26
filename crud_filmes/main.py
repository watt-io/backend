from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/filmes')
def get_all_movies(request: schemas.Filme):
    return request