class Filme:
    def __init__(self, id: int, titulo: str, diretor: str, ano: int):
        self.id = id
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

        # Métodos para conversão de dados
        def to_dict(self):
            """"Converte o objeto Filme em um dicionário"""
            return {
                "id": self.id,
                "titulo": self.titulo,
                "diretor": self.diretor,
                "ano": self.ano,
            }

        # Método estático para criar um objeto Filme a partir de um dicionário
        @staticmethod
        def from_dict(data: dict):
            """Cria um objeto Filme a partir de um dicionário."""
            return Filme(
                id=data["id"],
                titulo=data["titulo"],
                diretor=data["diretor"],
                ano=data["ano"],
            )