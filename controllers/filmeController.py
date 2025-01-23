from typing import List
from fastapi import APIRouter
from models.interfaces.filmeRepoInterface import FilmeRepoInterface
from models.filmeModel import FilmeModel, FilmeResponse

class FilmeController():

    def __init__(self, filmeRepo : FilmeRepoInterface):

        """
        Construtor da classe FilmeController.

        Args:
            filmeRepo (FilmeRepoInterface): Interface de repositório de filmes.

        Attributes:
            filmeRepo (FilmeRepoInterface): Interface de repositório de filmes.
            router (FastAPI.Routers): Roteador de endpoints da API.
        """

        self.filmeRepo = filmeRepo

        self.router = APIRouter(tags=["Filmes"])

        self.router.add_api_route("/filmes", self.get_filmes, methods=["GET"], response_model = List[FilmeResponse])
        self.router.add_api_route("/filmes", self.post_filme, methods=["POST"])
        self.router.add_api_route("/filmes/{id}", self.get_filme_by_id, methods=["GET"], response_model = List[FilmeResponse])

    def get_filmes(self):
        """
        Retorna todos os filmes

        Returns:
            List[FilmeResponse]: lista de filmes
        """
        return self.filmeRepo.get_filmes()

    def post_filme(self, filme: FilmeModel):
        """
        Cria um novo filme
        """

        return self.filmeRepo.post_filme(filme)

    def get_filme_by_id(self, id: int):
        """
        Retorna um filme pelo seu id

        Args:
            id (int): o id do filme a ser retornado

        Returns:
            List[FilmeResponse]: o filme com o id especificado
        """
        return self.filmeRepo.get_filme_by_id(id)


