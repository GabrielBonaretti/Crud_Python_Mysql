from conecta import conecta
from conecta import close

def deletar_conta(nome):
    conexao, cursor = conecta()

    comando = 'DELETE FROM usuarios WHERE nome = "{}"'.format(nome)
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    close(conexao=conexao, cursor=cursor) 
