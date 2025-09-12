from sqlalchemy.orm import Session
from Models.CategoryModel import Category
from DTOs.CategoryDTOs import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, book_data: CategoryCreate) -> Category:
        book = Category(**book_data.dict())
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def list_all(self, skip: int = 0, limit: int = 10, name: str | None = None):
        query = self.db.query(Category)
        if name:
            query = query.filter(Category.name == name)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, book_id: int):
        return self.db.query(Category).filter(Category.id == book_id).first()

    def update(self, book_id: int, book_data: CategoryCreate):
        book = self.get_by_id(book_id)
        if book:
            for field, value in book_data.dict().items():
                setattr(book, field, value)
            self.db.commit()
            self.db.refresh(book)
        return book
        
    def delete(self, book_id: int):
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
        return book
