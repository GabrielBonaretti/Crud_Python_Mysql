import mysql.connector

try:
    conecta()
except Exception as e:
    print(f"Erro de conexão {e}")


def listar_usuarios():
    cursor = conexao.cursor()
    cursor.execute('select database()')
    linha = cursor.fetchone()

    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    print(
        '{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format('ID', 'NOME', 'EMAIL', 'PLANO', 'TIPO', 'IDADE'))
    print('-' * 88)
    for i in linhas:
        print('{0:<3} | {1:<12} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))


def listar_filmes():
    cursor = conexao.cursor()
    cursor.execute('select database()')
    linha = cursor.fetchone()
    print(f'Banco => {linha[0]}\n')

    sql = "SELECT * from filmes"
    cursor.execute(sql)
    linhas = cursor.fetchall()

    print('{0:<3} | {1:<30} | {2:<40} | {3:<15} | {4:<5}'.format('ID', 'FILME', 'PLANO', 'DESCRIÇÃO', 'CLASSIFICAÇÃO'))
    print('-' * 88)
    for i in linhas:
        print('{0:<3} | {1:<30} | {2:<40} | {3:<15} | {4:<5}'.format(i[0], i[1], i[2], i[3], i[4]))