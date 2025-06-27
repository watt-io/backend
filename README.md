# Projeto de Teste com FastAPI, MySQL e Docker

Este projeto é uma aplicação desenvolvida em Python utilizando o framework **FastAPI**, com banco de dados **MySQL** para persistência dos dados, e orquestrada via **Docker** para facilitar o desenvolvimento e a implantação.

---

## Sobre o projeto

Este foi um projeto de aprendizado e teste, onde explorei pela primeira vez conceitos importantes como:

- Desenvolvimento de uma API RESTful com **FastAPI**;
- Persistência de dados em um banco de dados real, no caso o **MySQL**;
- Uso de **containers Docker** para isolamento dos serviços e ambiente replicável;
- Configuração de redes e volumes Docker para garantir a comunicação entre a API e o banco;

Todo o conhecimento foi adquirido de forma **autônoma**, com muita pesquisa e estudo principalmente a partir das documentações oficiais das ferramentas utilizadas. Foi uma oportunidade valiosa para entender como montar um ambiente completo e funcional com tecnologias modernas, desde o desenvolvimento até o deploy em containers.

---

## Tecnologias usadas

- Python 3.x  
- FastAPI  
- MySQL  
- Docker e Docker Compose  

---

## Como rodar o projeto

Para rodar o projeto certifique-se de estar no diretório "backend". Após isso basta executar o comando ***docker compose build*** para criar a imagem e depois o comando ***docker compose up*** para subir e executar o container.