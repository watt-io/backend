from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from Data.session import get_db
from Services.DirectorService import DirectorService
from DTOs.DirectorDTOs import DirectorCreate, DirectorResponse
from typing import List
from utils.auth import get_current_user

router_director = APIRouter(prefix="/directors", tags=["Directors"])

@router_director.post("/", response_model=DirectorResponse)
def create_director(director: DirectorCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = DirectorService(db)
    return service.create_director(director)

@router_director.get("/", response_model=List[DirectorResponse])
def list_directors(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: str | None = None,
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    service = DirectorService(db)
    return service.list_directors(page=page, page_size=page_size, name=name)

@router_director.get("/{id}", response_model=DirectorResponse)
def get_director(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = DirectorService(db)
    return service.get_director(id)

@router_director.put("/{id}", response_model=DirectorResponse)
def update_director(id: int, director: DirectorCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    service = DirectorService(db)
    return service.update_director(id, director)

@router_director.delete("/{id}")
def delete_director(id: int, db: Session = Depends(get_db)):
    service = DirectorService(db)
    return service.delete_director(id)
