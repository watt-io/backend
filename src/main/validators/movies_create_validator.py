from pydantic import BaseModel, ConfigDict, Field

class MovieCreateValidator(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, examples=["Rio"])
    director: str = Field(min_length=1, examples=["Carlos Saldanha"])
    release_year: int = Field(ge=1888, examples=[2011])
    genre: str = Field(min_length=1, examples=["Animação, Aventura, Comédia"])


class MovieOut(BaseModel):
    id: int = Field(examples=[1])
    title: str = Field(examples=["Rio"])
    director: str = Field(examples=["Carlos Saldanha"])
    release_year: int = Field(examples=[2011])
    genre: str = Field(examples=["Animação, Aventura, Comédia"])


class MovieCreateResponse(BaseModel):
    message: str = Field(examples=["Movie created successfully"])
    data: MovieOut


class MoviesListResponse(BaseModel):
    total: int = Field(examples=[1])
    data: list[MovieOut]


class MovieDetailResponse(BaseModel):
    data: MovieOut