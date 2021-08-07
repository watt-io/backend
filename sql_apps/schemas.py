from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    name: str
    description: str
    duration: str
    director: str
    release_date: str

    class Config:
        orm_mode = True
