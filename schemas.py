from pydantic import BaseModel

class FilmeBase(BaseModel):
    titulo: str

class FilmeRequest(FilmeBase):
    ...

class FilmeResponse(FilmeBase):
    id: int

    class Config:
        orm_mode = True