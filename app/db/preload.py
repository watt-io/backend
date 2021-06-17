from .operations.filmes import (
	add_movie,
	retrieve_movie
)

async def load() -> None:
	if await retrieve_movie('8364'):
		return

	await add_movie({ "id": "9207", "title": "The Week Of", "genre": "comedy", "release": "2018", "imdb": 5.2 })
	await add_movie({ "id": "6532", "title": "The Ridiculous 6", "genre": "action/comedy", "release": "2015", "imdb": 4.8 })
	await add_movie({ "id": "0c22", "title": "Sandy Wexler", "genre": "comedy", "release": "2017", "imdb": 5.2 })
	await add_movie({ "id": "8364", "title": "You Don't Mess with the Zohan", "genre": "comedy", "release": "2008", "imdb": 5.5 })
