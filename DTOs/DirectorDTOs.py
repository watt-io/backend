from pydantic import BaseModel, Field
from datetime import date

class DirectorBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=40, description="Nome do diretor")
    nationality: str = Field(..., min_length=2, max_length=40, description="Nacionalidade do diretor")
    birth_date: date | None = Field(None, description="Data de nascimento do diretor (opcional)")

class DirectorCreate(DirectorBase):
    pass

class DirectorResponse(DirectorBase):
    id: int

    class Config:
        orm_mode = True
