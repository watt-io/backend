import pydantic as _pydantic

class _BaseMovie(_pydantic.BaseModel):
    name: str
    genre: str
    release: int

class Movie(_BaseMovie):
    id: int

    class Config:
        orm_mode = True

class MovieCreate(_BaseMovie):
    pass