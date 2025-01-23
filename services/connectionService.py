import os
from utils.db import mySqlDb
from models.repos.filmeRepoMySQL import FilmeRepoMySQL


def determinar_conexao():
    """
    Determina qual conexão a ser utilizada com base no valor da variável de ambiente DB_TYPE.

    Returns:
        FilmeRepoInterface: Repositório de filmes
    """
    if os.getenv('DB_TYPE') == 'mysql':
        connectionMySql = mySqlDb.criar_conexao_mySql()
        repo = FilmeRepoMySQL(connectionMySql)

        return repo