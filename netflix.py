from conecta import conecta
from conecta import close
from read import listar_usuarios

class Cliente:  # comparar filme/usuario no banco
    def __init__(self, nome='' , senha='####', email='', plano='basico', tipo="user"):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.tipo = ["user", "admin"]
        if tipo in self.tipo:
            self.tipo = tipo
        else:
            print("Tipo inválido")
            self.tipo = ''
        self.plano = ["basico", "medio", "premium"]
        if plano in self.plano:
            self.plano = plano
        else:
            print("Plano inválido")
            self.plano = ''


    def verificar_usuario(email, senha):
        resultado = listar_usuarios()
        for i in range(len(resultado)):
            if email == resultado[i][3] and senha == resultado[i][2]:
                conta = Cliente(resultado[i][1], resultado[i][2], resultado[i][3], resultado[i][4], resultado[i][5])
                return conta


    def verificar_filme(plano_filme, plano_usuario):
        if plano_filme == "basico" and plano_usuario == "basico" or plano_filme == "basico" and plano_usuario == "medio" or plano_filme == "basico" and plano_usuario == "premuim" or plano_filme == "medio" and plano_usuario == "medio" or plano_filme == "medio" and plano_usuario == "premium" or plano_filme == "premium" and plano_usuario == "premium":
            print("pode")
        else:
            print("nao pode")