'''
2- Classificador de Idade


Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

'''

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Classificação: Criança")
elif 13 <= idade <= 17:
    print("Classificação: Adolescente")
elif 18 <= idade <= 59:
    print("Classificação: Adulto")
elif idade >= 60:
    print("Classificação: Idoso")
else:
    print("Idade inválida.")
