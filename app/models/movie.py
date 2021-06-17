from pydantic import (
	BaseModel,
	Field
)

class MovieSchema(BaseModel):
	id: str = Field(...)
	title: str = Field(...)
	genre: str = Field(...)
	release: str = Field(...)
	imdb: float = Field(..., gt=0.0, lt=10.0)

def ResponseModel(data, message):
	return {
		"data": [data],
		"code": 200,
		"message": message
	}

def ErrorResponseModel(error, code, message):
	return {
		"error": error,
		"code": code,
		"message": message
	}