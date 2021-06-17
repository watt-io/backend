import bson
import pydantic

class Movie(pydantic.BaseModel):
	_id: bson.ObjectId
	id: str
	title: str
	genre: str
	release: str
	imdb: float