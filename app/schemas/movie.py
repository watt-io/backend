from pydantic import BaseModel

class MovieBase(BaseModel):
    name: str
    description: str
    genre: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int
    
    class Config:
        orm_mode = True