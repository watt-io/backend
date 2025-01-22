class mySqlDbService:
    def __init__(self, connection):
        """
        Construtor da classe mySqlDbService.

        Args:
            connection (conexao mysql): Conexao com o banco de dados mysql
        """
        self.connection = connection

    def criar_banco(self, nome_banco):
        
        """
        Cria um banco de dados no MySQL se ele não existir.

        Esta função utiliza a conexão MySQL fornecida para criar um banco de dados
        com o nome especificado. Se o banco de dados já existir, ele não será recriado.

        Args:
            nome_banco (str): O nome do banco de dados a ser criado.
        """

        cursor = self.connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_banco}")
        cursor.execute(f"USE {nome_banco}")
        cursor.execute("CREATE TABLE IF NOT EXISTS filmes (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), diretor VARCHAR(255), ano_lancamento INT, genero VARCHAR(255))")
        self.connection.commit()
        print(f"Banco de dados '{nome_banco}' criado ou já existente.")