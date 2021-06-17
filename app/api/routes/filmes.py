import json
import fastapi

import app.models as models
import app.db.mongo as mongo
import app.libs.serializer as serializer

router = fastapi.APIRouter()

@router.get('/filmes/')
async def read_movies():
	database = mongo.dbLayer()
	movies_mongo_cursor = database.db['movies'].find({})

	# Here's a weird case in which we're serializing and deserializing an array of objects
	# First. Why the f*c8 it's doing it ? 🤡
	#
	# Well, fastapi doesn't have a method for using a custom subclass of JSONEncoder
	# to serialize custom data types such bson.ObjectId so I created a subclass
	# and used it with the standard json library from Python.
	movies = json.dumps([ movie for movie in movies_mongo_cursor ], cls=serializer.JSONEncoder)

	return json.loads(movies)

@router.get('/filmes/{id}')
async def read_movie(id: str):
	database = mongo.dbLayer()
	movie: models.Movie

	if movie := database.db['movies'].find_one({ 'id': id }):
		movie = json.dumps(movie, cls=serializer.JSONEncoder)
	else:
		raise fastapi.HTTPException(status_code=404, detail="Item not found")

	return json.loads(movie)

@router.post('/filmes/')
async def create_movie(item: models.Movie):
	database = mongo.dbLayer()
	database.db['movies'].insert_one(item.dict())

	return item