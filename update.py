from conecta import conecta
from conecta import close
import menu as mn


def update_usuario(sett, set_value, where, where_value):
    conexao, cursor = conecta()

    comando = 'UPDATE usuarios SET {} = "{}" WHERE nome = "{}"'.format(sett, set_value, where, where_value)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 


def update_filmes(sett, set_value, where, where_value):
    conexao, cursor = conecta()

    comando = 'UPDATE filmes SET {} = "{}" WHERE nome = "{}"'.format(sett, set_value, where, where_value)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 

