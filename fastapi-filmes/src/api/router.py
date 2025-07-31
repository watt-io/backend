from fastapi import APIRouter, Depends
from typing import List
from src.db.database import SessionLocal
from sqlalchemy.orm import Session
from src.schemas import Film, FilmCreate
from src.services import FilmService

router = APIRouter(prefix="/filmes", tags=["Filmes"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Film])
async def get_films(db: Session = Depends(get_db)):
    film_service = FilmService(db)
    return film_service.get_all_films()

@router.post("/", response_model=Film)
async def create_film(film: FilmCreate,db: Session = Depends(get_db)):
    film_service = FilmService(db)
    return film_service.create_film(film)

@router.get("/{id}")
def get_film(id: int, db: Session = Depends(get_db)):
    service = FilmService(db)
    return service.get_film(id)
