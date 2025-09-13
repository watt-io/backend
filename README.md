**🎬 API de Filmes com FastAPI**
- Uma API RESTful construída com FastAPI, SQLAlchemy e SQLite, que permite realizar operações de CRUD - (Criar, Ler, Atualizar, Deletar) em um catálogo de filmes. Ideal para estudos, protótipos ou como - - base para projetos maiores.


**🚀 Como rodar o projeto**
- Crie e ative o ambiente virtual:

- python -m venv venv
- source venv/bin/activate  # Linux/macOS
- venv\Scripts\activate     # Windows

**Instale as dependências:**
- pip install -r requirements.txt

**Execute a aplicação:**
- uvicorn app.main:app --reload

**Acesse no navegador:**
* http://127.0.0.1:8000/docs

**🐳 Rodando com Docker**

- Build e execução:
- docker-compose up --build

**Acesse no navegador:**
- http://localhost:8000/docs