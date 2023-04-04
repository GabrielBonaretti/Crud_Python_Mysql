import menu as mn
from read import listar_filmes
from create import criar_filme 
from create import criar_usuario
from netflix import Cliente
import update
import delete

def user():
    while True:
        escolha_usuario = mn.menu_user()

        if escolha_usuario == "Ver filmes":
            pass

        elif escolha_usuario == "Modificar dados":
            pass

        elif escolha_usuario == "Sair":
            break


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
            pass

        elif escolha_usuario == "Sair":
            x = False
        
def modificar_dados_admin(conta):
    resultado = mn.modificar_dados_admin()

    if resultado == "nome":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_nome_usuario(nome=modificacao, senha=conta.get("senha"))
        return True

    elif resultado == "senha":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_senha_usuario(senha=modificacao, nome=conta.get("nome"))
        return True

    elif resultado == "email":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_email_usuario(email=modificacao, nome=conta.get("nome"))
        return True

    elif resultado == "plano":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_plano_usuario(plano=modificacao, nome=conta.get("nome"))
        return True
    
    elif resultado == "tipo":
        modificacao = mn.modificar_dado(resultado=resultado)
        update.update_tipo_usuario(plano=modificacao, nome=conta.get("nome"))
        return True

    elif resultado == "apagar conta":
        delete.deletar_conta(nome=conta.get("nome"))
        return False


def main():
    while True:
        escolha = mn.menu_inicial()

        if escolha == "Cadastrar Usuário":
            nome, senha, email, plano, tipo = mn.cadastrar_usuario()
            criar_usuario(nome, senha, email, plano, tipo)

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
