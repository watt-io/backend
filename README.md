### Guia para inicialização do projeto 
1. Instalar a versão 3.11.0 do python;
2. Navegar para a raiz do projeto através do terminal;
3. Criar o ambiente virtual python pelo comando:

```
python3 -m venv nome_do_ambiente_virtual
```

4. Executar o comando abaixo para ativar o ambiente virtual;
* Windows
```
nome_do_ambiente_virtual\Scripts\activate
```
* Linux/MacOS
```
source nome_do_ambiente_virtual/bin/activate
```
5. Instalar as dependências pelo comando:
```
pip install -r requirements.txt
```
6. Executar o comando abaixo dentro da pasta `sql_app/` para iniciar o projeto;
```
uvicorn main:app --reload
``````
7. No navegador, acessar o projeto pela url [http://localhost:8000/docs#](http://localhost:8000/docs#)
