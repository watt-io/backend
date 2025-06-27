from core.models.movie import Movie
from core.ports.movie_interface import MovieInterface


class GetMovieByTitle:
    def __init__(self, repo: MovieInterface):
        self.repo = repo

    def execute(self, title: str) -> Movie | None:
        return self.repo.get_by_title(title)