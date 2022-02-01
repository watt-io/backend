import datetime as _dt
import pydantic as _pd


class _BaseMovie(_pd.BaseModel):
    title: str
    rating: float
    duration: float
    release_year: int


class Movie(_BaseMovie):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateMovie(_BaseMovie):
    pass
