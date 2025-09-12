from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from Data.session import get_db
from Services.FilmService import FilmService
from DTOs.FilmDTOs import FilmCreate, FilmResponse
from typing import List
from utils.auth import get_current_user
router_film = APIRouter(prefix="/films", tags=["Films"])

@router_film.post("/", response_model=FilmResponse)
def create_film(film: FilmCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = FilmService(db)
    return service.create_film(film)

@router_film.get("/", response_model=List[FilmResponse])
def list_films(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    title: str | None = None,
    category: str | None = None,
    language: str | None = None,
    release_year: int | None = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    service = FilmService(db)
    return service.list_films(
        page=page,
        page_size=page_size,
        title=title,
        category=category,
        language=language,
        release_year=release_year
    )

@router_film.put("/{id}", response_model=FilmResponse)
def update_film(id : int, film: FilmCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = FilmService(db)
    return service.update_film(id, film)

@router_film.delete("/{id}")
def delete_film(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = FilmService(db)
    return service.delete_film(id)
