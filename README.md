### Quick started

##### Requeriments:
Install ```docker```, ```docker-compose```

#### Clone:

``` -git clone -b feature/raian-barbosa https://github.com/raianb-dev/backend.git ```

In terminal: ```cd ./backend```, start aplication: ```docker-compose up```

#### Application route: ```localhost:8000``` and documentation in path: `/docs`

##### Routes:

 - `/v1/api/home` -  Methods GET
 - `/v1/api/movie` - Methods POST 
 - `/v1/api/movie/{id_movie}` - Methods GET * get by id
 - `/v1/api/movie/{id_movie}` -  Methods PUT
 - `/v1/api/movie/{id_movie}` -  Methods DELETE

##### About:

built with :

- FastAPI
- SQLAlchemy 
- SQLite 

##### Aditional automated test: 

start test:

- In repository ```./FastAPI.postman_collection.json```
- Import collection in Postman
- Run collection or folder. 
