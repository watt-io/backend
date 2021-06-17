import pydantic

class Movie(pydantic.BaseModel):
	id: str
	title: str
	genre: str
	release: str
	imdb: str