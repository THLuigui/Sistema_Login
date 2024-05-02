# Importando banco de dados
import sqlite3 as lite

# CRUD

# CREATE = Inserindo ou Criando items no banco de dado


# criando conexão
con = lite.connect('dados.db')


# Inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)


# READ = Acessar / Mostrar

# Acessar informações


def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista


# UPDATE = Atualizar
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Formulario SET nome=?, email=?, telefone=?, dia_em=? , estado=?, assunto=?  WHERE id=?"
        cur.execute(query, i)


# Delete - Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = " DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
