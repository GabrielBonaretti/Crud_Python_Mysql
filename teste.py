def soma(numero1, numero2):
    soma=numero1+numero2
    return soma

resultado_soma = soma(numero1=10, numero2=20)
print(resultado_soma)

resultado_soma = soma(numero1=1000, numero2=100)
print(resultado_soma)


teste_lista = ["gabriel", "teste"]
teste_lista.append("oi")
print(teste_lista)

print(teste_lista[0])
teste_matriz = [["gabriel", "teste"], 
                ["a", "b"]]

for i in range(len(teste_lista)):
    if teste_lista[i] == "teste":
        print("achou")
    else:
        pass

print(teste_matriz[1][0])