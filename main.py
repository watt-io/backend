from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MovieModel(BaseModel):
    id: int
    movie_name: str
    synopsis: str
    duration: int
    year_release: int
    movie_genre: str

@app.post('/filmes')
def register_movie(movie: MovieModel):
    return {'Mensagem': 'Filme cadastrado com sucesso!'}