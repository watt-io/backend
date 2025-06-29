# API FILMES

##  Como rodar o projeto

Em primeiro plano, clone este repositório em seu computador e acesse o seu diretorio.

### 1. Crie um ambiente virtual

    python -m venv .venv

### 2. Ative o ambiente virtual

Use um dos comandos abaixo:

Linux/macOS:

    source .venv/bin/activate

Windows:

    .venv\Scripts\activate

### 3. Instale as dependências
Após ativar o ambiente, instale as dependências com o comando:

    pip install -r requirements.txt

### 4. Inicie a aplicação

Use o comando abaixo para iniciar o servidor da API:

    uvicorn main:app --reload

### Acesse a API

API base: http://127.0.0.1:8000/

Para ter acesso a documentação gerada automaticamente use:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

