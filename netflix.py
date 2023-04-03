from read import listar_usuarios

class Cliente:  # comparar filme/usuario no banco
    def __init__(self, nome='' , senha='####', email='', plano='basico', tipo="user"):
        self.nome = nome
        self.senha = senha
        self.email = email

        self.tipo = ["user", "admin"]
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print("Tipo inválido")
            self.tipo = ''

        self.plano = ["basico", "medio", "premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            print("Plano inválido")
            self.plano = ''

    def verificar_usuario(email, senha):
        resultado = listar_usuarios()
        for i in resultado:
            if email == resultado[i][2] and senha == resultado[i][1]:
                conta = Cliente(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                return conta
            else:
                print("Algo está errado")