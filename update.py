from conecta import conecta
from conecta import close
import menu as mn


def update_nome_usuario(nome, senha):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET nome = "{}" WHERE senha = "{}"'.format(nome, senha)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 


def update_senha_usuario(senha, nome):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET senha = "{}" WHERE nome = "{}"'.format(senha, nome)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 


def update_email_usuario(email, nome):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET email = "{}" WHERE nome = "{}"'.format(email, nome)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 


def update_plano_usuario(plano, nome):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET plano = "{}" WHERE nome = "{}"'.format(plano, nome)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor)   


def update_tipo_usuario(tipo, nome):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET tipo = "{}" WHERE nome = "{}"'.format(tipo, nome)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor)   