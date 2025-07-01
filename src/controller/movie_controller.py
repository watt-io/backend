from src.models.movie import MovieModel
from src.repositories.movie_repository import MovieRepository

from fastapi import FastAPI, HTTPException

router = FastAPI()
movie_repository = MovieRepository

@router.post('/filmes', status_code=201)
def register_movie(movie: MovieModel):
    movie_repository.create(movie)
    return {
        'Mensagem': 'Filme registrado com sucesso!'
        }

@router.get('/filmes')
def get_all_movies():
    return movie_repository.get_all()

def get_one_movie(id: int):
    movie = movie_repository.get_by_id(id)
    if movie:
        return movie
    else:
        raise HTTPException(status_code=404, detail='Filme não encontrado :(')