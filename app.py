from flask import Flask, request, jsonify, make_response, Response
from typing import Optional
from db import get_db
from sqlalchemy.orm import Session
from model import Filmes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class Filme():
    titulo: str
    ano: Optional[int]
    genero: Optional[str]


@app.route("/filmes", methods=['GET'])
def selecionaFilmes(db):
    db = get_db
    filmes = Filmes.listarFilmes(db)
    filmes_json = Filmes.to_json
    return jsonify(
        message = 'Lista de filmes',
        data= filmes_json)



@app.route("/filmes/<id>", methods=['GET'])
def selecionaFilmeId(id: int, db=get_db):
    try:
        filme = Filmes.buscarFilmes(filme_id= id, db=db)
        return jsonify(
            message = 'Filme Selecionado',
            data= filme
        )
    except Exception as e:
        return {'message': "Erro ao buscar filme"}
    


@app.route("/filme/<id>", methods=["PUT"])
def atulizaFilme(id: int, filme_modificado, db=get_db):
    try:
        Filmes.atualizarFilme(filme_id=id, filme_mod=filme_modificado, db=db)
        return {"message":"Filme atualizado com sucesso"}
    except Exception as e:
        return {'message': "Erro ao atualizar filme"}



@app.route("/filme", methods="[POST]")
def cadastraFilme(filme=Filme, db=get_db):       
    try:
        novoFilme = Filmes(
            titulo = Filme.titulo,
            ano = Filme.ano,
            genero = Filme.genero
        )

        Filmes.criarFilme(filme = novoFilme, db=db)
        return {"message":"Filme cadastrado com sucesso"}

    except Exception as e:
        return  {'message': "Erro ao cadastrar filme"}
    

@app.route("/filme", methods="[DELETE]")
def deletaFilme(id: int, db= get_db):
    try:
        Filmes.deletarFilme(filme_id=id, db=db)
        return {"message":"Filme excluido com sucesso"}

    except Exception as e:
         return  {'message': "Erro ao excluir filme"}
app.run()