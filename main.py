from fastapi import FastAPI
from models import Filme, FilmePar

app = FastAPI()

#Get chamada filmes por qualquer parametro
@app.get("/filmes")
def chamarLista(titulo:str|None  = None,
    diretor:str|None = None,
    pais:str|None  = None,
    ano:str|None  = None,
    censura:str|None  = None,
    sinopse:str|None  = None):
    try:
        query = Filme.select()
        if(titulo):
            query = query.where(Filme.titulo == titulo)
        if(diretor):
            query = query.where(Filme.diretor == diretor)
        if(pais):
            query = query.where(Filme.pais == pais)
        if(ano):
            query = query.where(Filme.ano == ano)
        if(censura):
            query = query.where(Filme.censura == censura)
        if(sinopse):
            query = query.where(Filme.sinopse == sinopse)
        filmes = [filme for filme in query.dicts()]
        return filmes
    except:
        return {"Status":404, "Mensagem": "Erro ao chamar lista" }

#Inserir um novo filme
@app.post("/filmes")
def insereFilme(novoFilme:FilmePar):
    try:
        #Recebe os dados do novo filme que sera inserido
        filme = {
            'titulo' : novoFilme.titulo,
            'diretor' : novoFilme.diretor,
            'pais' : novoFilme.pais,
            'ano' :  novoFilme.ano,
            'censura' : novoFilme.censura,
            'sinopse' : novoFilme.sinopse
        }
        #Insere o filme no final da tabela
        Filme.insert(filme).execute()
        return {"Status":200, "Mensagem": "Inserido com suceso" }
    except:
       return {"Status":400, "Mensagem": "Não inserido" }

#Get chamada filme por id
@app.get("/filmes/{id}")
def encontrarFilme(id:int):
    try:
        filmeProcurado = Filme.get_by_id(id)
        return filmeProcurado.__data__
    except:
        return {"Status":404, "Mensagem": "Id não cadastrado" }



#Patch para atualizar os filmes no banco
@app.patch("/filmes/{id}")
def uptadeFilme(attFilme:FilmePar, id:int):
    try:
        #Encontra o filme pelo id
        filmeUpdate : Filme = Filme.get_by_id(id)

        #Atualiza e salva no banco os novos dados
        filmeUpdate.titulo = attFilme.titulo
        filmeUpdate.diretor = attFilme.diretor
        filmeUpdate.pais = attFilme.pais
        filmeUpdate.ano = attFilme.ano
        filmeUpdate.censura = attFilme.censura
        filmeUpdate.sinopse = attFilme.sinopse
        filmeUpdate.save()
        return {"Status":200, "Mensagem": "Atualizado com suceso" }
    except:
       return {"Status":400, "Mensagem": "Não inserido" }

#Exclui o filme por id
@app.delete("/filmes/{id}")
def apagarFilme(id:int):
    try:
        #Encontra o filme pelo id
        filmeApagado = Filme.get_by_id(id)
        #Apaga o filme selecionado
        filmeApagado.delete_instance()
        return {"Status":200, "Mensagem": "Filme excluído" }
    except:
        return {"Status":400, "Mensagem": "Filme não excluído" }