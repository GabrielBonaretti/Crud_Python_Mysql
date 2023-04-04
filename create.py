from conecta import conecta
from conecta import close

def criar_usuario(nome, senha, email, plano, tipo):
    conexao, cursor = conecta()

    comando = 'INSERT INTO usuarios (nome, senha, email, plano, tipo)' \
              ' VALUES ("{}", "{}", "{}", "{}", "{}")'.format(nome, senha, email, plano, tipo)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(cursor=cursor, conexao=conexao)


def criar_filme(nome, descricao, genero, plano):
    conexao, cursor = conecta()

    comando = 'INSERT INTO filmes (nome, descricao, genero, plano)' \
              ' VALUES ("{}", "{}", "{}", "{}")'.format(nome, descricao, genero, plano)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(cursor=cursor, conexao=conexao)
