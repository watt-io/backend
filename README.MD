# Como Subir a Aplicação

Este documento fornece instruções sobre como iniciar e usar a aplicação FastAPI para o CRUD de filmes.

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado o Python 3 e o gerenciador de pacotes pip. Além disso, é necessário ter o Docker instalado em seu sistema.

## Configuração

1. **Clonar o repositório**: Faça o clone do repositório da aplicação para o seu ambiente de desenvolvimento através do seguinte comando:
    ```
    git clone https://github.com/rodrigomjr99/backend.git
    ```

2. **Instalar as Dependências**: Navegue até o diretório do projeto e instale as dependências usando o pip:
    ```
    cd backend
    pip install -r requirements.txt
    ```

## Execução usando Docker

1. **Construir a Imagem Docker**: Execute o comando a seguir para construir a imagem Docker da aplicação:
    ```
    docker-compose build
    ```

2. **Iniciar os Contêineres Docker**: Use o Docker Compose para iniciar os contêineres:
    ```
    docker-compose up
    ```

3. **Acesso à Aplicação**: Após iniciar os contêineres, a aplicação estará disponível em http://localhost:8000

## Uso da Aplicação

Você pode usar a interface de documentação automática do FastAPI para testar e interagir com a API. Acesse `http://localhost:8000/docs` em seu navegador para ver a documentação e experimentar as diferentes rotas disponíveis.

## Encerramento da Aplicação

Para encerrar a execução da aplicação, pressione `Ctrl + C` no terminal onde os contêineres estão sendo executados. Em seguida, você pode parar os contêineres usando o Docker Compose através do seguinte comando:
    ```
    docker-compose down
    ```
Isso encerrará a execução dos contêineres Docker e liberará os recursos do sistema.
