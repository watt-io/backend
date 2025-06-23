from pydantic import BaseModel, ConfigDict


class CreateMovieSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    overview: str
    year: int
    rating: float
    category: str


class MovieSchema(CreateMovieSchema):
    id: int
