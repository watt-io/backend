from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies_db = []

class MovieModel(BaseModel):
    id: int
    movie_name: str
    synopsis: str
    duration: int
    year_release: int
    movie_genre: str

@app.post('/filmes')
def register_movie(movie: MovieModel):
    movies_db.append(movie)
    return {'Mensagem': 'Filme cadastrado com sucesso!'}

@app.get('/filmes')
def get_all_movies():
    return movies_db