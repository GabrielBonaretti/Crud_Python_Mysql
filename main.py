import menu as mn
from create import criar_usuario
from netflix import Cliente


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
                while True:
                    escolha_usuario = mn.menu_user()

                    if escolha_usuario == "Ver filmes":
                        pass

                    elif escolha_usuario == "Modificar dados":
                        pass

                    elif escolha_usuario == "Sair":
                        break
                


        elif escolha == "Sair":
            break


if __name__ == "__main__":
    main()
