from netflix import Cliente

usuario = []
usuarios = []
escolhido = ["####", "", "", "####"]
planos = ["basico", "medio", "premium"]
tipos = ["user", "admin"]


def menu():
    print("-------------------------\n"
              f"Usuário: {escolhido[0]}\n"
              f"Tipo: {escolhido[3]}\n"
              "[0] - Sair\n"
              "[1] - Cadastrar Usuário\n"
              "[2] - Cadastrar Filme\n"
              "[3] - Login\n"
              "[4] - Listar Filmes\n"
              "-------------------------")
        escolha = int(input("Digite: "))



