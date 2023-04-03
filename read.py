from conecta import conecta
from conecta import close
import mysql.connector

conexao, cursor = conecta()


def listar_usuarios():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista

    print(
        '{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format('ID', 'NOME', 'EMAIL', 'PLANO', 'TIPO', 'IDADE'))
    print('-' * 88)
    for i in resultado:
        print('{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))

    close(conexao=conexao, cursor=cursor)    
    return resultado

def listar_filmes():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista

    print(
        '{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format('ID', 'NOME', 'EMAIL', 'PLANO', 'TIPO', 'IDADE'))
    print('-' * 88)
    for i in resultado:
        print('{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
    
    close(conexao=conexao, cursor=cursor)    
    return resultado

