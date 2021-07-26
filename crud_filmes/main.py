from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/filmes')
def get_all_movies(request: schemas.Filme):
    return request