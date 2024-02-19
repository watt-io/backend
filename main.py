from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()

# Criar tabela de filmes se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    diretor TEXT,
                    ano INTEGER
                )''')
conn.commit()

# Operação Create (POST)
@app.post("/filmes")
def cadastrar_filme(titulo: str, diretor: str, ano: int):
    cursor.execute("INSERT INTO filmes (titulo, diretor, ano) VALUES (?, ?, ?)", (titulo, diretor, ano))
    conn.commit()
    return {"mensagem": "Filme cadastrado com sucesso"}

# Operação Read (GET)
@app.get("/filmes")
def listar_filmes():
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()
    return {"filmes": filmes}

@app.get("/filmes/{id}")
def buscar_filme_por_id(id: int):
    cursor.execute("SELECT * FROM filmes WHERE id=?", (id,))
    filme = cursor.fetchone()
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return {"filme": filme}

# Operação Update (PUT)
@app.put("/filmes/{id}")
def atualizar_filme(id: int, titulo: str, diretor: str, ano: int):
    cursor.execute("UPDATE filmes SET titulo=?, diretor=?, ano=? WHERE id=?", (titulo, diretor, ano, id))
    conn.commit()
    return {"mensagem": "Filme atualizado com sucesso"}

# Operação Delete (DELETE)
@app.delete("/filmes/{id}")
def deletar_filme(id: int):
    cursor.execute("DELETE FROM filmes WHERE id=?", (id,))
    conn.commit()
    return {"mensagem": "Filme deletado com sucesso"}
