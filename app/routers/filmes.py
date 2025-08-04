from fastapi import APIRouter
from schemas.filmes import Filme
from services.filmes import Filmes as FilmesService

router = APIRouter(
    prefix="/filmes",
    tags=["filmes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_filmes() -> list[Filme]:
    return await FilmesService().get_filmes()


@router.get("/{id}")
async def read_filme(id: int):
    return await FilmesService().get_filme(id)


@router.post("/")
async def create_filme(filme: Filme):
    return await FilmesService().create_filme(filme)
