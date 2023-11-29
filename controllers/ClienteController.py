from typing import List
import services.database as db;
import models.Cliente as cliente;


def incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO TB_ALUNO (nome_aluno, data_nascimento, sala_aluno) 
    VALUES (?,?,?)""",
    cliente.nome_aluno, cliente.data_nascimento, cliente.sala_aluno).rowcount
    db.cnxn.commit()

def selecionarByid(id):
    db.cursor.execute("SELECT * FROM TB_ALUNO WHERE nome_aluno = ?",id)
    costumerList = []

    for row in db.cursor.fetchall():
       costumerList.append(cliente.Cliente(row[0],row[1],row[2]))

    return costumerList[0]

def alterar(cliente):
    count = db.cursor.execute("""
    UPDATE TB_ALUNO 
    SET nome_aluno = ?, data_nascimento = ?, sala_aluno = ?
    WHERE nome_aluno = ?
    """,
    cliente.nome_aluno, cliente.data_nascimento, cliente.sala_aluno, cliente.nome_aluno).rowcount
    db.cnxn.commit()


def Excluir(nome_aluno):
    count = db.cursor.execute("""
    DELETE FROM TB_ALUNO WHERE nome_aluno = ?""",
    nome_aluno).rowcount
    db.cnxn.commit()

def selecionarTodos():
    db.cursor.execute("SELECT * FROM TB_ALUNO")
    costumerList = []

    for row in db.cursor.fetchall():
       costumerList.append(cliente.Cliente(row[0],row[1],row[2]))

    return costumerList


