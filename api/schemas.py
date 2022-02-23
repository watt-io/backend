from pydantic import BaseModel


class MovieBaseSchema(BaseModel):
    name: str


class CreateMovieSchema(MovieBaseSchema):
    name: str = ""


class MovieSchema(MovieBaseSchema):
    id: int
