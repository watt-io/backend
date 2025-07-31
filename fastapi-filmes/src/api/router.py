from fastapi import APIRouter
from typing import List
from src.schemas import Film, FilmCreate
from src.services import FilmService

router = APIRouter(prefix="/films", tags=["Films"])
film_service = FilmService()

@router.get("/filmes", response_model=List[Film])
async def get_films():
    return film_service.get_all_films()

@router.post("/filmes", response_model=Film)
async def create_film(film: FilmCreate):
    return film_service.create_film(film)
