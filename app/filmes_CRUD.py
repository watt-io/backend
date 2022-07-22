# CRUD -> Create Read Update Delete
import json
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from enum import Enum


class FilmeEnum(str, Enum):
    nome = "nome"
    ano = "ano"
    genero = "genero"
    duracao = "duracao"

class Filme(BaseModel):
    id: str 
    nome: str 
    ano: int
    genero: str 
    duracao: str 
        
    
class Crud():

    def create(self, id: str, nome: str, ano: int, genero: str, duracao: str):
        dict_filme_novo = {id: {'nome': nome, 'ano': ano, 'genero': genero, 'duracao': duracao}}
        with open('db.json', 'r+') as f:
            dict_atual = json.load(f)
            if id in dict_atual:
                f.close()
                raise HTTPException(status_code=412, detail="Id já existente")
            dict_atual.update(dict_filme_novo)
            dict_novo = json.dumps(dict_atual, indent=2)
            f.close()
        with open('db.json', 'w+') as file:
            file.write(dict_novo)
            file.close()
        return True 
    
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
            
    def update(self, id: str, campo, conteudo):
        with open('db.json', 'r') as f:
            dict_atual = json.load(f)
            f.close()
        if id not in dict_atual:
            raise HTTPException(status_code=404, detail="Id não encontrada")
        if campo == 'ano':
            conteudo = int(conteudo)
        dict_atual[id][campo] = conteudo
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
                                              