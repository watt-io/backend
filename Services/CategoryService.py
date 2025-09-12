from fastapi import HTTPException
from sqlalchemy.orm import Session
from Repositories.CategoryRepository import CategoryRepository
from DTOs.CategoryDTOs import CategoryCreate

class CategoryService:
    def __init__(self, db: Session):
        self.repo = CategoryRepository(db)

    def create_category(self, category_data: CategoryCreate):
        return self.repo.create(category_data)

    def list_categories(self, page: int = 1, page_size: int = 10, name: str | None = None):
        # Validando a paginação
        if page < 1: page = 1
        if page_size < 1: page_size = 10
        skip = (page - 1) * page_size
        categories =  self.repo.list_all(skip=skip, limit=page_size, name=name)
        if not categories:
            raise HTTPException(status_code=404, detail="Categoria não encontrada.")
        return categories

    def get_category(self, category_id: int):
        category = self.repo.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Categoria não encontrada.")
        return category

    def update_category(self, category_id: int, category_data: CategoryCreate):
        category = self.repo.update(category_id, category_data)
        if not category:
            raise HTTPException(status_code=404, detail="Categoria não encontrada.")
        return category

    def delete_category(self, category_id: int):
         
        category=self.repo.delete(category_id)
        if not category:
             raise HTTPException(status_code=404, detail="Categoria não encontrada")
        return category
