![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/` - [GET] rota de teste para verificar se está tudo certo
 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.
 - `/filmes/` - [PUT] deve atualizar o filme com ID especificado
 - `/filmes/{id}` - [DELETE] deve deletar o filme com ID especificado

O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

#### Ferramentas 

- Orientação a objetos
- FastAPI
- Docker
- MySQL

#### Como executar

- Clone a branch e sincronize todos os arquivos
- Abra o terminal e na pasta raiz execute o comando ```docker-compose up --build -d``` que realizará o build e inicializará o mesmo
- A aplicação deverá rodar na porta 80, enquanto o banco de dados na porta 3306 (portas padrões)
- A pasta collections contém arquivos referentes à collection e ao environment do postman que foram utilizados para testar a aplicação

#### Dúvidas?

Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para samuelmangia@gmail.com | samuel.mangia@geb.inatel.br

### Observação

O arquivo .env foi commitado apenas para facilitar o processo de execução. Comumente, é enviado um env.example e não as credenciais originais.

Salve!
