import os
import sys
import inquirer

list = [("a", "abc", "abcdef"),("f", "fed", "fedcba")]
filmes = []

for i in range(len(list)):
        filmes.append(list[i][0]+ "|" +list[i][1]+ "|" +list[i][2])
        print(filmes)

questions = [
        inquirer.List(
            "escolha",
            message="Você deseja: ",
            choices=filmes,
        ),
    ]

answers = inquirer.prompt(questions)

