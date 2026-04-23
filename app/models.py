from sqlalchemy import Column, Integer, String
from app.database import Base

class Filme(Base):
    """
    Representação da tabela 'filmes' no banco de dados.
    Motivo: O paradigma de Orientação a Objetos mapeia classes para tabelas (ORM),
    eliminando a necessidade de escrever queries SQL puras para operações básicas.
    """
    # Nome da tabela no banco de dados
    __tablename__ = "filmes"

    # Chave primária, autoincremento, com índice para buscas rápidas
    id = Column(Integer, primary_key=True, index=True)
    
    # Coluna para o título, não pode ser nula
    titulo = Column(String, nullable=False)
    
    # Coluna para o diretor
    diretor = Column(String, nullable=False)
    
    # Coluna para o ano de lançamento
    ano_lancamento = Column(Integer, nullable=False)