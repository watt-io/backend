### **Descrição**

Neste desafio foi solicitado a criação de um CRUD para o cadastro de filmes, foi utilizada FASTAPI juntamente com o banco de dados relacional postgres com o ORM  e SQLAlchemy e também com Docker e Docker Compose.

Foi utilizado técnicas de injeção de dependências para diminuir o acoplamento das regras de negócios com as controllers do projetos, com isso facilitando uma possível manutenção e a realização dos testes unitários. Foi aplicado também alguns princípios de Clean Architecture e SOLID.


Rotas da API:

 - `/filmes` -       [POST] deve cadastrar um novo filme.
 - `/filmes` -       [GET] deve retornar todos os filmes cadastrados.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.
 - `/filmes` -       [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` -       [PUT] atualizar os dados de um filme.
 - `/filmes/{id}` -  [DELETE] apagar um filme cadastrado.


#### **Forma para rodar o projetos**

Na raiz do projeto rode o comando ``` docker-compose build ``` para gerar a imagem da aplicação juntamente com o banco de dados após isso deverá rodar ``` docker-compose up ``` ou ``` docker-compose up -d ``` fica a sua escolha, neste momento ele ir iniciar o banco de dados e aplicação e irá aplicar as migrações do banco de dados

#### **Documentação**

Para acessar a documentação apó inicializar a aplicação esse sera a o endereço [/docs](http://localhost:8081/docs) ou http://localhost:8081/docs


