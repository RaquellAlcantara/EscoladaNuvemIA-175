'''
4- Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
'''
def idade_em_dias(ano_nascimento: int, ano_atual: int) -> int:
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias
