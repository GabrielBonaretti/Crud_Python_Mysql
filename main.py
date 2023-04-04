import menu as mn
from read import listar_filmes
from create import criar_filme 
from create import criar_usuario
from netflix import Cliente
import update
import delete


def user(conta):
    x = True
    while x is True:
        escolha_usuario = mn.menu_user()

        if escolha_usuario == "Ver filmes":
            resultado = listar_filmes()
            print(resultado)
            filme_escolhido = mn.filmes(lista_filmes=resultado)
            Cliente.verificar_filme(plano_filme=filme_escolhido[4], plano_usuario=conta.get("plano"))

        elif escolha_usuario == "Modificar dados":
            x = modificar_dados_user(conta=conta)

        elif escolha_usuario == "Sair":
            x = False


def modificar_dados_user(conta):
    resultado = mn.modificar_dados_user()

    if resultado == "nome":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett=resultado, set_value=modificacao, where="email", where_value=conta.get("email"))
        return True

    elif resultado == "senha":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett=resultado, set_value=modificacao, where="email", where_value=conta.get("email"))
        return True

    elif resultado == "email":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett=resultado, set_value=modificacao, where="senha", where_value=conta.get("senha"))
        return True

    elif resultado == "apagar conta":
        delete.deletar_conta(nome=conta.get("email"))
        return False


def admin(conta):
    x = True
    while x is True:
        escolha_usuario = mn.menu_admin()

        if escolha_usuario == "Ver filmes":
            resultado = listar_filmes()
            filme_escolhido = mn.filmes(lista_filmes=resultado)
            Cliente.verificar_filme(plano_filme=filme_escolhido[4], plano_usuario=conta.get("plano"))

        elif escolha_usuario == "Modificar dados":
            modificar_dados_admin(conta=conta)
            
        elif escolha_usuario == "Adicionar Filmes":
            nome_filme, descricao, genero_filme, plano_filme = mn.cadastrar_filmes()
            criar_filme(nome=nome_filme, descricao=descricao, genero=genero_filme, plano=plano_filme)

        elif escolha_usuario == "Modificar Filmes":
            resultado = listar_filmes()
            filme_escolhido = mn.filmes(lista_filmes=resultado)
            modificar_dados_filmes(filme=filme_escolhido)
            
        elif escolha_usuario == "Sair":
            x = False

        
def modificar_dados_filmes(filme):
    resultado = mn.modificar_dados_filmes()

    if resultado == "nome":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_filmes(sett="nome", set_value=modificacao, where="descricao", where_value=filme[2])
        return True

    elif resultado == "descricao":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_filmes(sett="descricao", set_value=modificacao, where="nome", where_value=filme[1])
        return True

    elif resultado == "genero":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_filmes(sett="genero", set_value=modificacao, where="descricao", where_value=filme[2])
        return True

    elif resultado == "plano":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_filmes(sett="plano", set_value=modificacao, where="descricao", where_value=filme[2])
        return True
    
    elif resultado == "apagar filme":
        delete.deletar_filme(nome=filme[1])
        return False


def modificar_dados_admin(conta):
    resultado = mn.modificar_dados_admin()

    if resultado == "nome":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett="nome", set_value=modificacao, where="email", where_value=conta.get("email"))
        return True

    elif resultado == "senha":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett="senha", set_value=modificacao, where="email", where_value=conta.get("email"))
        return True

    elif resultado == "email":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett="email", set_value=modificacao, where="senha", where_value=conta.get("senha"))
        return True

    elif resultado == "plano":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett="plano", set_value=modificacao, where="email", where_value=conta.get("email"))
        return True
    
    elif resultado == "tipo":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_usuario(sett="tipo", set_value=modificacao, where="email", where_value=conta.get("email"))
        return True

    elif resultado == "apagar conta":
        delete.deletar_conta(nome=conta.get("email"))
        return False


def main():
    while True:
        escolha = mn.menu_inicial()

        if escolha == "Cadastrar Usuário":
            nome, senha, email, plano, tipo = mn.cadastrar_usuario()
            criar_usuario(nome=nome, senha=senha, email=email, plano=plano, tipo=tipo)

        elif escolha == "Logar Usuário":
            email, senha = mn.logar_usuario()
            conta = vars(Cliente.verificar_usuario(email, senha))

            if conta.get("tipo") == "user":
                user(conta=conta)

            elif conta.get("tipo") == "admin":
                admin(conta=conta)


        elif escolha == "Sair":
            break


if __name__ == "__main__":
    main()
