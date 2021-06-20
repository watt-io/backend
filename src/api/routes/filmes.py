from typing import List
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from src.models.filmes import FilmeCreate, FilmePublic
from src.db.repositories.filmes import FilmeRepository
from src.api.dependencies.database import get_repository


router = APIRouter()

@router.get("/")
async def get_all_filmes() -> List[dict]:
	filmes = [
		{"id": 1, "tittle":"A VERY PYTHONIC MOVIE"},
		{"id": 2, "tittle":"Bee Movie"}
	]
	return filmes

@router.post("/", response_model=FilmePublic, name="filmes:create-filme", status_code=HTTP_201_CREATED)
async def create_new_filme(
	new_filme: FilmeCreate = Body(..., embed=True),
	filme_repo: FilmeRepository = Depends(get_repository(FilmeRepository)),
) -> FilmePublic:
	print(new_filme)
	create_filme = await filme_repo.create_filme(new_filme=new_filme)
	return create_filme