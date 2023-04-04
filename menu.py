import os
import sys
import inquirer

sys.path.append(os.path.realpath("."))


def menu_filmes():
    
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=[],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def menu_inicial():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Cadastrar Usuário", "Logar Usuário", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def menu_user():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Ver filmes", "Modificar dados", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def menu_admin():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["Ver filmes", "Modificar dados", "Adicionar Filmes", "Modificar Filmes", "Ver usuários", "Sair"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def logar_usuario():
    questions = [
        inquirer.Text("email", message="E-mail"),
        inquirer.Text("senha", message="Senha"),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("email"), answers.get("senha")


def cadastrar_usuario():
    questions = [
        inquirer.Text("nome", message="Nome"),
        inquirer.Text("senha", message="Senha"),
        inquirer.Text("email", message="E-mail"),
        inquirer.Text("plano", message="Plano(basico/medio/premium)"),
        inquirer.Text("tipo", message="Tipo(user/admin)"),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("nome"), answers.get("senha"), answers.get("email"), answers.get("plano"), answers.get("tipo")


def cadastrar_filmes():
    questions = [
        inquirer.Text("nome_filme", message="Nome"),
        inquirer.Text("descricao", message="Descrição"),
        inquirer.Text("genero_filme", message="Gênero"),
        inquirer.Text("plano_filme", message="Plano"),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("nome_filme"), answers.get("descricao"), answers.get("genero_filme"), answers.get("plano_filme")


def filmes(lista_filmes):
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=lista_filmes,
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def modificar_dados_admin():
    questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=["nome", "senha", "email", "plano", "tipo", "apagar conta"],
        ),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("escolha")


def modificar_dado(resultado):
    questions = [
        inquirer.Text("modificacao", message="{}".format(resultado)),
    ]

    answers = inquirer.prompt(questions)

    return answers.get("modificacao")