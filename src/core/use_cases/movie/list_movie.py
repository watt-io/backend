from core.models.movie import Movie
from core.ports.movie_interface import MovieInterface


class ListMovie:
    def __init__(self, repo: MovieInterface):
        self.repo = repo

    def execute(self) -> list[Movie]:
        return self.repo.list()