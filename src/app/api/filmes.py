from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.api.models import FilmeDB, FilmeSchema

router = APIRouter()


@router.post("/", response_model=FilmeDB, status_code=201)
async def create_filme(payload: FilmeSchema):
    filme_id = await crud.post(payload)

    response_object = {
        "id": filme_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.get("/{id}/", response_model=FilmeDB)
async def read_filme(id: int = Path(..., gt=0),):
    filme = await crud.get(id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme not found")
    return filme


@router.get("/", response_model=List[FilmeDB])
async def read_all_filmes():
    return await crud.get_all()

