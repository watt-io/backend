import json
from typing import List
from app.models import Filme

DATABASE = "filmes.json"

def carregar_dados() -> List[Filme]:
    try:
        with open(DATABASE, "r") as f:
            filmes = json.load(f)
            return [Filme.from_dict(filme) for filme in filmes]
    except FileNotFoundError:
        return []
    
def salvar_dados(filmes: List[Filme]) -> None:
    with open(DATABASE, "w") as f:
        json.dump([filme.to.dict() for filme in filmes], f, indent=4)