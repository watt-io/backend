from typing import List
from fastapi import APIRouter
from models.interfaces.filmeRepoInterface import FilmeRepoInterface
from models.filmeModel import FilmeModel, FilmeResponse

class FilmeController():

    def __init__(self, filmeRepo : FilmeRepoInterface):

        self.filmeRepo = filmeRepo

        self.router = APIRouter()

        self.router.add_api_route("/filmes", self.get_filmes, methods=["GET"], response_model = List[FilmeResponse])
        self.router.add_api_route("/filmes", self.post_filme, methods=["POST"])
        self.router.add_api_route("/filmes/{id}", self.get_filme_by_id, methods=["GET"], response_model = List[FilmeResponse])

    def get_filmes(self):
        return self.filmeRepo.get_filmes()

    def post_filme(self, filme: FilmeModel):
        return self.filmeRepo.post_filme(filme)

    def get_filme_by_id(self, id: int):
        return self.filmeRepo.get_filme_by_id(id)


