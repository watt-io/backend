from warnings import catch_warnings
from pydantic import BaseModel
import peewee

#Criação do banco de dados
banco_dados = peewee.SqliteDatabase('lista_de_filmes.db')

#Criação da modelo da tabela de filmes
class _BaseModel(peewee.Model):
    class Meta:
        database = banco_dados

class Filme(_BaseModel):
    titulo = peewee.CharField(unique=True)
    diretor = peewee.CharField()
    pais = peewee.CharField()
    ano =  peewee.CharField()
    censura = peewee.CharField()
    sinopse = peewee.TextField()

#Criação do modelo de filme para atualizar e inserir
class FilmePar(BaseModel):
    titulo : str
    diretor : str
    pais : str
    ano :  str
    censura : str
    sinopse : str


if __name__ == '__main__':
        try:
            Filme.create_table()
            print("Tabela 'Filmes' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'Filmes' já existe")