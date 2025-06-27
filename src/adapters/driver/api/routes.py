from fastapi import APIRouter
import uuid
from .schemas import MovieCreate, MovieRead
from adapters.driven.repositories.movie_repository_impl import SQLAlchemyMovieRepository
from core.use_cases.movie.add_movie import AddMovie
from core.use_cases.movie.list_movie import ListMovie
from core.use_cases.movie.get_movie_by_id import GetMovieById
from core.use_cases.movie.update_movie import UpdateMovie
from core.use_cases.movie.delete_movie_by_title import DeleteMovieByTitle
from core.models.movie import Movie
from http import HTTPStatus


router = APIRouter()

repo = SQLAlchemyMovieRepository()
add_movie_use_case = AddMovie(repo)
list_movie_use_case = ListMovie(repo)
get_movie_by_id_use_case = GetMovieById(repo)
update_movie_use_case = UpdateMovie(repo)
delete_movie_by_title_use_case = DeleteMovieByTitle(repo)


@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/filmes", response_model=list[MovieRead], status_code=HTTPStatus.OK)
def list_filmes():
    return list_movie_use_case.execute()

@router.post("/filmes", response_model=MovieRead, status_code=HTTPStatus.CREATED)
def add_filme(filme: MovieCreate):
    movie = Movie(
        id=str(uuid.uuid4()),
        title=filme.title,
        year=filme.year,
        duration=filme.duration
    )
    add_movie_use_case.execute(movie)
    return movie

@router.get("/filmes/{id}", response_model=MovieRead, status_code=HTTPStatus.OK)
def get_filme(id: str):
    movie = get_movie_by_id_use_case.execute(id)
    if not movie:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Filme não encontrado")
    return movie

@router.put("/filmes/{id}", response_model=MovieRead, status_code=HTTPStatus.OK)
def update_filme(id: str, filme: MovieCreate):
    movie = Movie(id=id, title=filme.title, year=filme.year, duration=filme.duration)
    updated = update_movie_use_case.execute(movie)
    if not updated:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Filme não encontrado para atualizar")
    return movie

@router.delete("/filmes/{title}", status_code=HTTPStatus.NO_CONTENT)
def delete_filme(title: str):
    deleted = delete_movie_by_title_use_case.execute(title)
    if not deleted:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Filme não encontrado para deletar")
    return