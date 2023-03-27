def conecta():
    conexao = mysql.connector.connect(
        host='localhost',
        database='netflix',
        user='root',
        password=''
    )