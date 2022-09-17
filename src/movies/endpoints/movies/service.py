from filmes.endpoints.filmes.repository import MoviesRepository


class MoviesService:
    def __init__(self, movies_repository: MoviesRepository):
        self.movies_repository = movies_repository

    def get_all(self):
        return self.movies_repository.get_all()

    def get_by_id(self, id: int):
        return self.movies_repository.get_by_id(id)

    def create(self, name: str, description: str):
        return self.movies_repository.create(name=name, description=description)

    def update(self, id: int, name: str, description: str):
        return self.movies_repository.update(id=id, name=name, description=description)

    def delete(self, id: int):
        return self.movies_repository.delete(id=id)

    