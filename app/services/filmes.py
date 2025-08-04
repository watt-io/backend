from repository.filmes import create_filme, get_filme, get_filmes
from schemas.filmes import Filme


class Filmes:

    def __init__(self):
        pass

    async def get_filmes(self):
        return await get_filmes()

    async def get_filme(self, id: int):
        return await get_filme(id)

    async def create_filme(self, filme: Filme):
        return await create_filme(filme)
