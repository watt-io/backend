from pydantic import BaseModel, Field

class FilmeBase(BaseModel):
    """
    Schema base contendo os atributos comuns de um filme.
    Motivo: Evita repetição de código (DRY - Don't Repeat Yourself).
    """
    # Usamos o Field para adicionar validações e descrições na documentação (Swagger)
    titulo: str = Field(..., description="Título do filme")
    diretor: str = Field(..., description="Nome do diretor")
    ano_lancamento: int = Field(..., description="Ano de lançamento do filme", gt=1800)

class FilmeCreate(FilmeBase):
    """
    Schema usado especificamente para a criação (POST).
    Herda de FilmeBase. Neste caso simples, não adicionamos novos campos,
    mas se houvesse senhas ou dados sensíveis de entrada, ficariam aqui.
    """
    pass

class FilmeResponse(FilmeBase):
    """
    Schema usado para formatar a resposta da API (GET e POST).
    Adiciona o campo 'id' que é gerado pelo banco de dados.
    """
    id: int

    class Config:
        # Permite que o Pydantic leia dados de objetos do SQLAlchemy, não apenas de dicionários
        from_attributes = True