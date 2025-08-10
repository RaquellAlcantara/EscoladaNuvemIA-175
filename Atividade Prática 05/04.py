'''
4- Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
'''

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 

try:
    ano = int(input("Digite o ano de nascimento: "))
    if ano > date.today().year or ano < 1900:
        raise ValueError("Ano inválido.")
    
    dias = idade_em_dias(ano)
    print(f"Idade em dias: {dias} dias")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
