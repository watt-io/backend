from core.models.movie import Movie
from core.ports.movie_interface import MovieInterface


class DeleteMovieByTitle:
    def __init__(self, repo: MovieInterface):
        self.repo = repo

    def execute(self, title: str) -> None:
        movie = self.repo.get_by_title(title)
        if movie:
            self.repo.delete(movie)
        else:
            raise ValueError(f"O filme '{title}' não foi encontrado. Verifique o título e tente novamente.")