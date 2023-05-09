import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='bdyoutube',
    user='root',
    password=''
)

cursor = conexao.cursor()

# crud

# =-=-=Crud=-=-=
# =-=-=Create=-=-=
# nome_produto = "chocolate"
# valor = 15
# comando = 'INSERT INTO vendas (nome_produto, valor) VALUES ("{}", {})'.format(nome_produto, valor)
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados (create, update, delete)

# =-=-=cRud=-=-=
# =-=-=Read=-=-=
# comando = 'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()  # ler o banco de dados (read)  # retorna uma lista
# print(resultado)

# =-=-=crUd=-=-=
# =-=-=Update=-=-=
# nome_produto = "todynho"
# valor = 6
# comando = 'UPDATE vendas SET valor = {} WHERE nome_produto = "{}"'.format(valor, nome_produto)
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados (create, update, delete)

# =-=-=cruD=-=-=
# =-=-=Delete=-=-=
# nome_produto = "todinho"
# comando = 'DELETE FROM vendas WHERE nome_produto = "{}"'.format(nome_produto)
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados (create, update, delete)

cursor.close()
conexao.close()
