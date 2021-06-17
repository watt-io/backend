from .. import mongo

# define the MongoDB Instance globally into the module
mongo = mongo.dbLayer()

async def add_movie(movie_data: dict) -> dict:
	if await mongo.db.get_collection('movies').find_one({'id': movie_data['id']}):
		return {
			"error": "An error occurred.",
			"code": 403,
			"message": "Movie ID already exists."
		}

	movie = await mongo.db.get_collection('movies').insert_one(movie_data)
	inserted_movie = await mongo.db.get_collection('movies').find_one({'_id': movie.inserted_id}, projection={'_id': False})

	return inserted_movie


# retrieve all present movies in the Database
async def retrieve_movies():
	movies = []
	async for movie in mongo.db.get_collection('movies').find(projection={'_id': False}):
		movies.append(movie)

	return movies


# retrieve a movie from the database with a matching ID
async def retrieve_movie(movie_id: str) -> dict:
	movie = await mongo.db.get_collection('movies').find_one({'id': movie_id}, projection={'_id': False})
	if movie:
		return movie
