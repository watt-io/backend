from typing import List
from models.interfaces.filmeRepoInterface import FilmeRepoInterface
from models.filmeModel import FilmeModel, FilmeResponse

class FilmeRepoMySQL(FilmeRepoInterface):
    def __init__(self, conexao_mysql):
        """
        Construtor da classe FilmeRepoMySQL

        Args:
            conexao_mysql (conexao mysql): Conexao com o banco de dados mysql
        """
        self.conexao = conexao_mysql

    def get_filmes(self) -> List[FilmeResponse]:
        """
        Retorna todos os filmes
        """
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM filmes")
        rows = cursor.fetchall()
        filmes = []
        for row in rows:
            filmes.append(FilmeResponse(
                id=row[0],
                titulo=row[1],
                diretor=row[2],
                ano_lancamento=row[3],
                genero=row[4]
            ))
        return filmes

    def post_filme(self, filme: FilmeModel) -> FilmeModel:
        """
        Cria um novo filme
        """
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano_lancamento, genero) VALUES (%s, %s, %s, %s)",
                       (filme.titulo, filme.diretor, filme.ano_lancamento, filme.genero))
        self.conexao.commit()
        return filme

    def get_filme_by_id(self, id: int) -> FilmeResponse:
        """
        Retorna um filme pelo seu id
        """
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return FilmeResponse(
            id=row[0],
            titulo=row[1],
            diretor=row[2],
            ano_lancamento=row[3],
            genero=row[4]
        )
