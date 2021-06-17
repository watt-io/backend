from typing import List

import fastapi

import app.models as models
import app.db.mongo as mongo

router = fastapi.APIRouter()

@router.get('/filmes/')
async def read_movies():
	database = mongo.dbLayer()
	movies_mongo_cursor = database.db['movies'].find({})

	movies: List[models.Movie] = list()

	for movie in movies_mongo_cursor:
		del movie['_id'] 
		movies.append(movie)

	return movies

@router.get('/filmes/{id}')
async def read_movie(id: str):
	database = mongo.dbLayer()
	movie: models.Movie

	if movie := database.db['movies'].find_one({ 'id': id }):
		del movie['_id']
	else:
		raise fastapi.HTTPException(status_code=404, detail="Item not found")

	return movie

@router.post('/filmes/')
async def create_movie(item: models.Movie):
	database = mongo.dbLayer()
	database.db['movies'].insert_one(item.dict())

	return item