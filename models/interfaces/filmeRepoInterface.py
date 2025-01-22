from typing import List
from models.filmeModel import FilmeModel

class FilmeRepoInterface:
    def get_filmes(self) -> List[FilmeModel]:
        """
        Retorna todos os filmes
        """
        pass

    def post_filme(self, filme: FilmeModel) -> FilmeModel:
        """
        Cria um novo filme
        """
        pass

    def get_filme_by_id(self, id: int) -> FilmeModel:
        """
        Retorna um filme pelo seu id
        """
        pass
