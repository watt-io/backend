from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True


class MovieCreate(BaseModel):
    name: str
    description: str | None = None

    class Config:
        orm_mode = True
