### FastAPI CRUD de Filmes
Este é um projeto de exemplo usando o framework FastAPI para criar uma API CRUD (Create, Read, Update, Delete) de filmes. A aplicação utiliza um banco de dados SQLite para persistência de dados.

### Configuração do Banco de Dados
O banco de dados é configurado usando SQLAlchemy, e a URL de conexão está definida como sqlite:///./test.db. O arquivo do banco de dados será criado no diretório do projeto como test.db. A tabela films contém colunas para id (chave primária), title, director, e year.

### Configuração da Aplicação FastAPI
A aplicação FastAPI é configurada com rotas para realizar operações CRUD nos filmes. As operações são definidas da seguinte forma:

Criar Filme (POST): Rota /filmes para criar um novo filme.
Listar Filmes (GET): Rota /filmes para obter todos os filmes cadastrados.
Obter Filme por ID (GET): Rota /filmes/{film_id} para obter detalhes de um filme específico.

### Modelos de Dados
FilmCreate: Usado para validar os dados recebidos nas requisições POST. Este modelo é utilizado na criação de um novo filme.
Execução do Projeto
### Requisitos
Python 3.11 ou superior instalado
Instalação das Dependências
bash
Copy code
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install python-dotenv

### Execução Sem Docker
Clone o repositório:

bash
Copy code
git clone https://github.com/watt-io/backend.git
cd seu_projeto
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copy code
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute o servidor FastAPI:

bash
Copy code
uvicorn main:app --reload
Acesse a API em http://localhost:8000/docs para explorar a documentação interativa da API.

### Execução Com Docker
Clone o repositório:

bash
Copy code
git clone https://github.com/watt-io/backend.git
cd seu_projeto
Construa a imagem Docker:

bash
Copy code
docker-compose build
Inicie a aplicação com Docker Compose:

bash
Copy code
docker-compose up -d
Acesse a API em http://localhost:8000/docs para explorar a documentação interativa da API.

#### Parar e Limpar
Sem Docker
Para o servidor pressionando Ctrl + C no terminal.
Com Docker
Pare a aplicação:

bash
Copy code
docker-compose down
Isso encerrará a execução do servidor e removerá os contêineres associados.


