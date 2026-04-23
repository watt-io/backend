# 🎬 Movie API

> API RESTful para gerenciamento de catálogo de filmes  
> RESTful API for movie catalog management

---

## 🌐 Languages
- 🇧🇷 [Português](#-português)
- 🇺🇸 [English](#-english)

---

# 🇧🇷 Português

## 📌 Sobre o Projeto
API REST desenvolvida para gerenciar um catálogo de filmes, com foco em:

- Arquitetura limpa (Clean Architecture)
- Tipagem estática
- Documentação automática
- Boas práticas de engenharia de software

---

## 🛠️ Tecnologias

- **Python 3.11+**
- **FastAPI** — alta performance e documentação automática
- **SQLAlchemy** — ORM robusto
- **SQLite** — banco leve e simples
- **Docker & Docker Compose** — ambiente isolado e replicável

---

## 🚀 Como Executar

### 🐳 Opção 1 — Docker (Recomendado)

```bash
docker-compose up --build
```

Acesse:
👉 http://localhost:8000

---

### 💻 Opção 2 — Ambiente Local

#### 1. Criar ambiente virtual
```bash
python -m venv venv
```

#### 2. Ativar ambiente

- Windows:
```bash
.\venv\Scripts\activate
```

- Linux/macOS:
```bash
source venv/bin/activate
```

#### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

#### 4. Rodar servidor
```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentação da API

Após iniciar o projeto:

- 🔍 Swagger UI:  
  http://localhost:8000/docs

- 📄 ReDoc:  
  http://localhost:8000/redoc

---

## 📌 Endpoints

### 🎥 Movies

| Método | Endpoint         | Descrição                     |
|--------|----------------|------------------------------|
| GET    | `/filmes`       | Lista todos os filmes        |
| POST   | `/filmes`       | Cria um novo filme           |
| GET    | `/filmes/{id}`  | Retorna detalhes de um filme |

---

## 📥 Exemplo de Payload

```json
{
  "titulo": "Interestelar",
  "diretor": "Christopher Nolan",
  "ano_lancamento": 2014
}
```

---

## 📂 Estrutura do Projeto (Sugestão)

```
app/
├── main.py
├── models.py
├── schemas.py
├── logger.py
├── routers/
├──────  movies.py
├── database.py
```

---

## 🧠 Diferenciais

- Código limpo e escalável
- Fácil integração com frontend
- Pronto para produção (com ajustes mínimos)
- Containerização completa

---

# 🇺🇸 English

## 📌 About the Project

This RESTful API was built to manage a movie catalog, focusing on:

- Clean Architecture
- Static typing
- Automatic documentation
- Software engineering best practices

---

## 🛠️ Technologies

- **Python 3.11+**
- **FastAPI** — high-performance framework
- **SQLAlchemy** — powerful ORM
- **SQLite** — lightweight database
- **Docker & Docker Compose** — containerized environment

---

## 🚀 How to Run

### 🐳 Option 1 — Docker (Recommended)

```bash
docker-compose up --build
```

Access:
👉 http://localhost:8000

---

### 💻 Option 2 — Local Environment

#### 1. Create virtual environment
```bash
python -m venv venv
```

#### 2. Activate environment

- Windows:
```bash
.\venv\Scripts\activate
```

- Linux/macOS:
```bash
source venv/bin/activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Start server
```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After running the project:

- 🔍 Swagger UI:  
  http://localhost:8000/docs

- 📄 ReDoc:  
  http://localhost:8000/redoc

---

## 📌 Endpoints

### 🎬 Movies

| Method | Endpoint         | Description                  |
|--------|----------------|--------------------------------|
| GET    | `/filmes`       | List all movies               |
| POST   | `/filmes`       | Create a new movie            |
| GET    | `/filmes/{id}`  | Get movie details             |

---

## 📥 Example Payload

```json
{
  "titulo": "Interstellar",
  "diretor": "Christopher Nolan",
  "ano_lancamento": 2014
}
```

---

## 📂 Project Structure (Suggested)

```
app/
├── main.py
├── models.py
├── schemas.py
├── logger.py
├── routers/
├──────  movies.py
├── database.py
```

---

## 🧠 Highlights

- Clean and maintainable code
- Easy frontend integration
- Production-ready foundation
- Fully containerized