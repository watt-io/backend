from core.models.movie import Movie
from core.ports.movie_interface import MovieInterface


class GetMovieById:
    def __init__(self, repo: MovieInterface):
        self.repo = repo

    def execute(self, movie_id: int) -> Movie | None:
        return self.repo.get_by_id(movie_id)