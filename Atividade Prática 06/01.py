'''
1- Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
'''
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Informe o tamanho da senha desejada: "))
    if tamanho <= 0:
        raise ValueError("O tamanho deve ser maior que zero.")
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
except Exception as e:
    print(f"Erro: {e}")
