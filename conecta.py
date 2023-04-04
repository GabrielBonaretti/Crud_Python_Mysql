import mysql.connector


def conecta():
    try:
        conexao = mysql.connector.connect(
            # HOST=aws.connect.psdb.cloud
            # USERNAME=vp7y8l27gk4z21wcup1u
            # PASSWORD=pscale_pw_hNOtqJrAiykvjyUAYVZRQDFg6Z5huCzXVcgy5K39SqT
            # DATABASE=database
            
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
