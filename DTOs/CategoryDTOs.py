from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=40, description="Nome da categoria de filme")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id : int

    class Config:
        orm_mode = True