from conecta import conecta
from conecta import close

def listar_usuarios():
    conexao, cursor = conecta()

    comando = 'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista
    
    close(conexao=conexao, cursor=cursor)    
    return resultado

def listar_filmes():
    conexao, cursor = conecta()

    comando = 'SELECT * FROM filmes'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista
    
    close(conexao=conexao, cursor=cursor)    
    return resultado

