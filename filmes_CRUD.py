# CRUD -> Create Read Update Delete
import json
from fastapi import FastAPI, HTTPException, status

from requests import delete

class Filme():
    def __init__(self, id: str, nome: str, ano: int, genero: str, duracao: str):
        self.__id = id
        self.__nome = nome
        self.__ano = ano
        self.__genero = genero
        self.__duracao = duracao
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_ano(self):
        return self.__ano
    
    def get_genero(self):
        return self.__genero
    
    def get_duracao(self):
        return self.__duracao
    
    def set_dict(self):
        ret_dict = {self.__id: {'nome': self.__nome, 'ano': self.__ano, 'genero': self.__genero, 'duracao': self.__duracao}}
        return ret_dict
    
class Crud():

    def create(self, id: str, nome: str, ano: int, genero: str, duracao: str):
        filme = Filme(id, nome, ano, genero, duracao)
        dict_filme_novo = filme.set_dict()
        with open('db.json', 'r+') as f:
            dict_atual = json.load(f)
            dict_atual.update(dict_filme_novo)
            dict_novo = json.dumps(dict_atual, indent=2)
            f.close()
        with open('db.json', 'w+') as file:
            file.write(dict_novo)
            file.close()
    
    def read(self):
        with open('db.json', 'r') as f:
            dict_atual = json.load(f)
            f.close()
        return dict_atual
    
    def read_by_id(self, id: str):
        with open('db.json', 'r') as f:
            dict_atual = json.load(f)
            f.close()
        if id not in dict_atual:
           raise HTTPException(status_code=404, detail="Id não encontrada")
        else:
            return dict_atual[id]
            
    def update(self, id: str, oq_mudar: str, conteudo):
        with open('db.json', 'r') as f:
            dict_atual = json.load(f)
            f.close()
        if id not in dict_atual:
            raise HTTPException(status_code=404, detail="Id não encontrada")
        if oq_mudar not in dict_atual[id]:
            raise HTTPException(status_code=404, detail="campo não encontrado")
        dict_atual[id][oq_mudar] = conteudo
        with open('db.json', 'w+') as f:
            json_string = json.dumps(dict_atual, indent=2)
            f.write(json_string)
            f.close()
        return dict_atual[id]     
        
    
    def delete(self, id: str):
        with open('db.json', 'r') as f:
            dict_atual = json.load(f)
            if id in dict_atual:
                dict_atual.pop(id)
                f.close()
            else:
                f.close()
                raise HTTPException(status_code=404, detail="Id não encontrada")         
        with open('db.json', 'w+') as f:
            dict_novo = json.dumps(dict_atual, indent=2)
            f.write(dict_novo)
            f.close() 
        return {"Sucesso": "filme deletado com sucesso"}       
                                              