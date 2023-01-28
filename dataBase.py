
import sqlite3

def inserir_filmes(titulo, ano):
    conn = sqlite3.connect("filmes.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO filmes (tirulo, ano) VALUES (?, ?)", (titulo, ano)
    )
    conn.commit()
    cursor.close()
    conn.close()

def ler_filmes():
    conn = sqlite3.connect("filmes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall() 
    cursor.close()
    conn.close()
    return filmes


def filme_especifico(id):
    conn = sqlite3.connect("filmes.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM filmes WHERE id=?", (id,))
    filmes = cursor.fetchall()    
    cursor.close()
    conn.close()
    return filmes
    

def mudar_filme_especifico(novo_titulo, novo_ano):
    conn = sqlite3.connect("filmes.db")
    cursor = conn.cursor()
    x = cursor.execute("UPDATE filmes SET titulo = ?, ano = ? WHERE id = ?", (novo_titulo, novo_ano, id))
    cursor.close()
    conn.close()
    return x

