import mysql.connector

def conecta():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='netflix',
            user='root',
            password=''
        )
        return conexao
    except Exception as e:
        print(f"Erro de conexão {e}")
        