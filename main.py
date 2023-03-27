def main():
    while True:
        escolha = menu()
        
        if escolha == 0:
            break

        elif escolha == 1:
            nome = input("Nome: ")
            usuario.append(nome)
            email = input("Email: ")
            usuario.append(email)
            while True:
                plano = input("Plano [basico | medio | premium]: ")
                if plano in planos:
                    usuario.append(plano)
                    break
                else:
                    print("Plano inválido")

            while True:
                tipo = input("Tipo [User | Admin]: ")
                if tipo in tipos:
                    usuario.append(tipo)
                    break
                else:
                    print("Plano inválido")

            usuarios.append(usuario[:])
            usuario.clear()
            print(usuarios)

        elif escolha == 3:
            escolhido.clear()
            busca_nome = input("Digite seu nome: ")
            for i in range(len(usuarios)):
                if busca_nome == usuarios[i][0]:
                    for x in range(4):
                        escolhido.append(usuarios[i][x])
                    break

menu()
b1 = Cliente(nome=escolhido[0], email=escolhido[1], plano=escolhido[2], tipo=escolhido[3])
b1.ver_filme("Rambo", "premium")


if __init__ == "__main__":
    main()