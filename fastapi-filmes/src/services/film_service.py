from typing import List
from src.schemas import FilmCreate, Film

class FilmService:
    def __init__(self):
        self._films = []
        self._id_counter = 1

    def get_all_films(self) -> List[Film]:
        return self._films

    def create_film(self, film_create: FilmCreate) -> Film:
        film = Film(id=self._id_counter, **film_create.dict())
        self._films.append(film)
        self._id_counter += 1
        return film
