import fastapi
from fastapi.encoders import jsonable_encoder

from app.db.operations.filmes import (
	add_movie,
	retrieve_movie,
	retrieve_movies
)

from app.models.movie import (
	MovieSchema,
	ResponseModel,
	ErrorResponseModel
)

router = fastapi.APIRouter()

@router.get('/filmes/', response_description="Movies retrieved")
async def read_movies():
	movies = await retrieve_movies()
	if movies:
		return ResponseModel(movies, "Movies data retrieved successfully.")

	return ResponseModel(movies, "Empty list returned")

@router.get('/filmes/{id}', response_description="Movie data retrieved")
async def read_movie(id: str):
	movie = await retrieve_movie(id)
	if movie:
		return ResponseModel(movie, "Movie data retrieved successfully.")

	return ErrorResponseModel("An error occurred.", 404, "Movie not found.")

@router.post('/filmes/', response_description="Movie data added into the database")
async def create_movie(item: MovieSchema = fastapi.Body(...)):
	movie = jsonable_encoder(item)
	new_movie = await add_movie(movie)

	if new_movie.get('error'):
		return ErrorResponseModel(new_movie["error"], new_movie["code"], new_movie["message"])

	return ResponseModel(new_movie, "Movie added successfully.")