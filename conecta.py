import mysql.connector


def conecta():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='netflix',
            user='root',
            password=''
        )

        cursor = conexao.cursor()

        return conexao, cursor
    except Exception as e:
        print(f"Erro de conexão {e}")


def close(cursor, conexao):
    cursor.close()
    conexao.close()