from conecta import conecta
import mysql.connector

conexao = conecta()

def inserir_filme():
    filme = input("Digite o nome do filme: ")
    plano_filme = input("Digite o plano do filme: ")
    descricao = input("Digite a descrição do filme: ")
    classificacao = int(input("Digite a classificação: "))

    inserir_filmes = """INSERT INTO filmes(filme, plano_filme, descricao, classificacao)
    values
    ("{}", "{}", "{}", {});
     """.format(filme, plano_filme, descricao, classificacao)

    cursor = conexao.cursor()
    cursor.execute(inserir_filmes)
    conexao.commit()

    sql = "SELECT * from filmes"
    cursor.execute(sql)
    linhas = cursor.fetchall()

    print('{0:<3} | {1:<30} | {2:<40} | {3:<8} | {4:<5}'.format('ID', 'FILME', 'PLANO', 'DESCRIÇÃO', 'CLASSIFICAÇÃO'))
    print('-' * 88)
    for i in linhas:
        print('{0:<3} | {1:<30} | {2:<40} | {3:<8} | {4:<5}'.format(i[0], i[1], i[2], i[3], i[4]))

def inserir_usuario():
    usuario = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    plano = input("Digite o plano do usuário: ")
    tipo = input("Digite o tipo do usuário: ")
    idade = int(input("Digite a idade do usuário: "))

    inserir_usuarios = """INSERT INTO usuarios(usuario, email, plano, tipo, idade)
    values
    ("{}","{}", "{}", "{}", {});
    """.format(usuario, email, plano, tipo, idade)

    cursor = conexao.cursor()
    cursor.execute(inserir_usuarios)
    conexao.commit()

    sql = "SELECT * from usuarios"
    cursor.execute(sql)
    linhas = cursor.fetchall()

    print('{0:<3} | {1:<30} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format('ID', 'USUÁRIO', 'EMAIL', 'PLANO', 'TIPO', 'IDADE'))
    print('-' * 88)
    for i in linhas:
        print('{0:<3} | {1:<30} | {2:<40} | {3:<8} | {4:<5} | {5:<5}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))