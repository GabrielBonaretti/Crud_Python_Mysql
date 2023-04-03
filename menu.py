import os
import sys
import inquirer

sys.path.append(os.path.realpath("."))


def menu_inicial():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Cadastrar Usuário", "Logar Usuário", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()


def menu_user():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Ver filmes", "Modificar dados", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()


def menu_admin():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Ver filmes", "Modificar dados", "Adicionar Filmes", "Modificar Filmes", "Ver usuários", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()


def logar_usuario():
    questions = [
        inquirer.Text("email", message="E-mail: "),
        inquirer.Text("senha", message="Senha: "),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()


def cadastrar_usuario():
    questions = [
        inquirer.Text("nome", message="Nome: "),
        inquirer.Text("senha", message="Senha: "),
        inquirer.Text("email", message="E-mail: "),
        inquirer.Text("plano", message="Plano(basico/medio/premium): ".islower()),
        inquirer.Text("tipo", message="Tipo(user/admin): ".islower()),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()


def cadastrar_filmes():
    questions = [
        inquirer.Text("nome_filme", message="Nome: "),
        inquirer.Text("plano_filme", message="Plano: "),
        inquirer.Text("descricao", message="Descrição: "),
    ]

    answers = inquirer.prompt(questions)

    return answers.values()
