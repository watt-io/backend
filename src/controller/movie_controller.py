from src.models.movie import MovieModel
from src.repositories.movie_repository import MovieRepository

from fastapi import APIRouter, HTTPException
from psycopg2.errors import UniqueViolation

router = APIRouter()
movie_repository = MovieRepository()

@router.post('/filmes', status_code=201)
def register_movie(movie: MovieModel):
    try:
        movie_repository.create(movie)
        return {
            'Mensagem': 'Filme registrado com sucesso!'
            }
    except UniqueViolation:
        raise HTTPException(status_code=409, detail=f'O filme {movie.movie_name} já está cadastrado.')
    except Exception as e:
        raise HTTPException(status_code=500, detail='Ocorreu um erro interno no servidor.')

@router.get('/filmes')
def get_all_movies():
    return movie_repository.get_all()

@router.get('/filmes/{id}')
def get_one_movie(id: int):
    movie = movie_repository.get_by_id(id)
    if movie:
        return movie
    else:
        raise HTTPException(status_code=404, detail='Filme não encontrado :(')