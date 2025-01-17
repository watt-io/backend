from typing import List, Optional
from app.models import Filme
from app.database import carregar_dados, salvar_dados

# Função para listar todos os filmes
def listar_filmes() -> List[Filme]:
    return carregar_dados()

# Função para criar um novo filme
def criar_filme(novo_filme: Filme) -> Filme:
    filmes = carregar_dados()
    filmes.append(novo_filme)
    salvar_dados(filmes)
    return novo_filme

# Função para obter um filme por ID
def obter_filme_por_id(filme_id: int) -> Optional[Filme]:
    filmes = carregar_dados()
    for filme in filmes:
        if filme.id == filme_id:
            return filme
    return None
