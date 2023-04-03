from conecta import conecta
from conecta import close

# import mysql.connector

conexao, cursor = conecta()


def criar_usuario(nome, senha, email, plano, tipo):
    comando = 'INSERT INTO netflix (nome, senha, email, plano, tipo)' \
              ' VALUES ("{}", "{}", "{}", "{}", "{}")'.format(nome, senha, email, plano, tipo)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(cursor=cursor, conexao=conexao)
