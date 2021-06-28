import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from api import Movies


movie = FastAPI()

class MovieData(BaseModel):
    filme: Optional[str]
    movie_id: Optional[str]


@movie.get("/filmes")
def get_all_movies() -> List[str]:

    listar = Movies.list_all()
    return False if not listar else listar


@movie.post("/filmes")
def persist(movie: MovieData = None):

    post = Movies(movie.filme).insert_movie()
    return False if not post[0] else True


@movie.get("/filmes/{movie_id}")
def get_unique_movie(movie_id: str) -> str:
    print(movie_id)
    unique = Movies(movie_id=movie_id).unique_movie()
    return False if not unique else unique


if __name__ == '__main__':
    uvicorn.run(movie, port=8000)