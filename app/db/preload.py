from .mongo import dbLayer

def load() -> None:
	database = dbLayer()
	if database.db['movies'].find_one({ "id": "8364" }):
		return

	database.db['movies'].insert_many([
		{ "id": "9207", "title": "The Week Of", "genre": "comedy", "release": "2018", "imdb": 5.2 },
		{ "id": "6532", "title": "The Ridiculous 6", "genre": "action/comedy", "release": "2015", "imdb": 4.8 },
		{ "id": "0c22", "title": "Sandy Wexler", "genre": "comedy", "release": "2017", "imdb": 5.2 },
		{ "id": "8364", "title": "You Don't Mess with the Zohan", "genre": "comedy", "release": "2008", "imdb": 5.5 }
	])