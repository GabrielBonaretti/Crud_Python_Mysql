class Cliente:
    def __init__(self, nome='', senha='', email='', plano='basico', tipo="user"):
        self.nome = nome
        self.senha = senha
        self.email = email

        self.tipos = ["user", "admin"]
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print("Tipo inválido")
            self.tipo = ''

        self.planos = ["basico", "medio", "premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            print("Plano inválido")
            self.plano = ''

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme=None):
        if self.plano == "premium" or self.plano == plano_filme:
            print("O cliente {} pode assistir o filme {}.".format(self.nome, filme))
        elif self.plano == "medio" and plano_filme == "basico":
            print("O cliente {} não pode assistir o filme {}.".format(self.nome, filme))
        else:
            print("O cliente {} não pode assistir o filme {}.".format(self.nome, filme))
