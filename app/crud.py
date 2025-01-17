import json

DATABASE = "filmes.json"

def carregar_dados():
    try:
        with open(DATABASE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def salvar_dados(dados):
    with open(DATABASE, "w") as f:
        json.dump(dados, f, indent=4)

def listar_filmes():
    return carregar_dados()

def criar_filme(filme):
    filmes = carregar_dados()
    filmes.append(filme.dict())
    salvar_dados(filmes)
    return(filme)

def obter_filme_por_id(filme_id):
    filmes = carregar_dados()
    for filme in filmes:
        if filme["id"] == filme_id:
            return filme
    return None