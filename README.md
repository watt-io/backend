![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

Implementação de uma CRUD de filmes para avaliação no processo seletivo de estágio na INOWATT.


Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.

Todas as rotas anteriormente foram implementas.

#### Como rodar a aplicação? 
Primeiro é preciso baixar a aplicação do GitHub. Após baixar para rodar a aplicação deve se
as dependencias em `.`:
`docker build -t mybackend .`
Criada a imagem da aplicação, agora é só utilizar o `docker-compose up` e a aplicação estará
rodando. Para ir ao o swagger basta acessar: http://0.0.0.0:8000/docs#/

- A aplicação utiliza de integração com banco de dados SqLite


#### Como começar?

Qualquer sugestão de melhoria, dúvida. Favor entrar em contato


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
