# CRUD -> Create Read Update Delete
import json

class Filme():
    def __init__(self, id: int, nome: str, ano: int, genero: str, duracao: str):
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
    
class crud():

    def create(self, id: int, nome: str, ano: int, genero: str, duracao: str):
        filme = Filme(id, nome, ano, genero, duracao)


if __name__ == '__main__':
    
    dict_filmes = {
    1: {'nome': 'forrest gump', 'ano': 1994, 'genero': 'drama', 'duracao': '142 min'},
    2: {'nome': 'drive', 'ano': 2011, 'genero': 'acao', 'duracao': '100 min'},
    3: {'nome': 'blade runner 2049', 'ano': 2017, 'genero': 'ficcao cientifica', 'duracao': '163 min'},
    4: {'nome': 'se7en', 'ano': 1995, 'genero': 'crime', 'duracao': '127 min'},
    5: {'nome': '1917', 'ano': 2019, 'genero': 'guerra', 'duracao': '119 min'},
}

string_json = json.dumps(dict_filmes, indent=2)
with open ('db.json', 'w') as f:
    f.write(string_json)