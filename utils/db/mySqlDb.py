import mysql.connector
from mysql.connector import Error
import os

def criar_conexao_mySql():
    """
    Cria uma conex o com o banco de dados mySql.

    Esta fun o cria uma conex o com o banco de dados mySql
    utilizando a biblioteca mysql-connector-python. Ela
    verifica se a conex o foi estabelecida com sucesso e
    retorna a conex o criada.

    Returns:
        connection: Uma conex o com o banco de dados mySql
    Raises:
        Error: Se houver um erro ao conectar com o banco de dados
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database='filmes_db'
        )
        if connection.is_connected():
            print("Conexão com o banco de dados mySql estabelecida com sucesso!")
            return connection
    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        raise e