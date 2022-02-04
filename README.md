![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.

O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

#### Sugestão de Ferramentas 
Não é obrigatório utilizar todas as as tecnologias sugeridas, mas será um diferencial =]

- Orientação a objetos (utilizar objetos, classes para manipular os filmes)
- [FastAPI](https://fastapi.tiangolo.com/) (API com documentação auto gerada)
- [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Aplicação deverá ficar em um container docker, e o start deverá seer com o comando ``` docker-compose up ```
- Integração com banco de dados (persistir as informações em json (iniciante) /[SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) / outros DB)


#### Como começar?

- Fork do repositório
- Criar branch com seu nome ``` git checkout -b feature/ana ```
- Faça os commits de suas alterações ``` git commit -m "[ADD] Funcionalidade" ```
- Envie a branch para seu repositório ``` git push origin feature/ana ```
- Navegue até o [Github](https://github.com/), crie seu Pull Request apontando para a branch **```main```**
- Atualize o README.md descrevendo como subir sua aplicação

#### Dúvidas?

Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para hendrix@wattio.com.br

Salve!

#### Solução

Este projeto é uma proposta de implementação simples, através da linguagem Python e Framework FastApi, de uma Api capaz de cadastrar e retornar informações sobre filmes.

Para rodar o projeto, certifique-se de ter instalado e configurado corretamente a linguagem Python 3, bem como todas as dependências necessárias.

Recomenda-se o uso da instalação do pacote de ambiente virtual (Virtual Environment).

Primeiro, certifique-se de ter o pacote Pip instalado. Pip é uma ferramenta poderosa usada para gerenciar e instalar pacotes na linguagem Python. Usando um sistema Ubuntu, execute os comandos no terminal:
- sudo apt update
- sudo apt install python3-pip

Verifique se a instalação foi finalizada corretamente através do comando no terminal:
- pip3 --version

Com isso, pode-se instalar o pacote de ambiente virtual. Se utilizando de um sistema Ubuntu, execute via terminal de comandos:
- pip3 install virtualenv

Agora, com o pacote instalado, deve-se criar um novo ambiente virtual para o projeto. A partir da pasta raiz do projeto e utilizando-se do sistema Ubuntu nesse caso, execute no terminal de comandos:
- virtualenv venv

Será criada uma nova pasta no projeto com o novo ambiente virtual, de nome "venv".

Precisamos ativar esse ambiente criado. Execute no terminal de comandos, também na pasta raiz do projeto:
- source venv/bin/activate

Agora, será necessário instalar os pacotes necessários para o uso do framework FastApi. No terminal de comandos do Ubuntu, execute:
- pip3 install fastapi uvicorn

Por fim, basta se iniciar o servidor da aplicação. A partir do diretório raiz do projeto, execute o comando no terminal:
- uvicorn main:WattIoBackendChallengeApi --reload

O projeto já estará rodando e o servidor da aplicação disponível. Para acessar a documentação, utilize os seguintes endpoints:
- http://localhost:8000/docs
- http://localhost:8000/redoc

Através da documentação auto-gerada pelo framework, pode-se visualizar os endpoints criados para o uso da aplicação, bem como os parâmetros necessários para cada um deles.
Tem-se as rotas:
- http://localhost:8000/filmes - [GET] retorna todos os filmes cadastrados.
- http://localhost:8000/filmes/{movie_id} - [GET] retorna as informações apenas do filmes especificado pelo seu id (uuid4).
- http://localhost:8000/filmes - [POST] cadastra um novo filme. Verifique os parâmtros necessários para a passagem do corpo na documentação.

As informações de cada filme não estão armazenadas em um banco de dados. Por hora, ficam armazenadas em uma lista de um objeto "Filme", que vai sendo incrementada a cada novo cadastro. Sugestões de melhoria no código incluem a troca para a persistência dessas informações em algum banco de dados, e também pode ser considerado o uso de Docker para subir um container de execução da aplicação.