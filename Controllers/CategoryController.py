from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from Data.session import get_db
from Services.CategoryService import CategoryService
from DTOs.CategoryDTOs import CategoryCreate, CategoryResponse
from typing import List
from utils.auth import get_current_user

router_category = APIRouter(prefix="/categories", tags=["Categorys"])

@router_category.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db),  current_user = Depends(get_current_user)):
    service = CategoryService(db)
    return service.create_category(category)


@router_category.get("/", response_model=List[CategoryResponse])
def list_categories(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: str | None = None,
    db: Session = Depends(get_db),
     current_user = Depends(get_current_user)
):
    service = CategoryService(db)
    return service.list_categories(page=page, page_size=page_size, name=name)



@router_category.put("/{id}", response_model=CategoryResponse)
def update_category(id : int, category: CategoryCreate, db: Session = Depends(get_db),  current_user = Depends(get_current_user)):
    service = CategoryService(db)
    return service.update_category(id, category)


@router_category.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db),  current_user = Depends(get_current_user)):
    service = CategoryService(db)
    return service.delete_category(id)
