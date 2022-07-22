from os.path import dirname, realpath, isfile
import json


class Json_manager():
    
    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'
        
    def cria_json(self, arq):
        dict_filmes = {
            '1': {'nome': 'forrest gump', 'ano': 1994, 'genero': 'drama', 'duracao': '142 min'},
            '2': {'nome': 'drive', 'ano': 2011, 'genero': 'acao', 'duracao': '100 min'},
            '3': {'nome': 'blade runner 2049', 'ano': 2017, 'genero': 'ficcao cientifica', 'duracao': '163 min'},
            '4': {'nome': 'se7en', 'ano': 1995, 'genero': 'crime', 'duracao': '127 min'},
            '5': {'nome': '1917', 'ano': 2019, 'genero': 'guerra', 'duracao': '119 min'},
            }
        path_data_json = self.path + arq
        
        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                string_json = json.dumps(dict_filmes, indent=2)
                f.write(string_json)
            return True
        else:    
            return False
        