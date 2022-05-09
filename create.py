import peewee
import csv
from models import Filme

#Faz a leitura do arquivo cvs
file = open('netflix_titles.csv',encoding='UTF-8')
reader = csv.reader(file)

#Conta o numero de filmes inseridos 
cont=0

listaFilmes = []
print('Inserindo filmes no banco...')
#Percorre a lista de programas e seleciona somente os filmes
for line in reader:
    if line[1] != 'Movie':
        continue
    filme = {
        'titulo':line[2],
        'diretor':line[3],
        'pais': line[5],
        'ano':  line[7],
        'censura': line[8],
        'sinopse': line[11]
    }
    #Adiciona o filme no final da lista
    listaFilmes.append(filme)
    cont+=1
    #Insere a Lista no banco de dados
    if len(listaFilmes) == 100:
        Filme.insert_many(listaFilmes).execute()
        listaFilmes.clear()
if len(listaFilmes) > 0:
    Filme.insert_many(listaFilmes).execute()
    listaFilmes.clear()        
print('Foram inseridos ' + str(cont) + ' filmes')