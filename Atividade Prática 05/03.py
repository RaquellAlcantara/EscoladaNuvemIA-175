'''
3- Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
'''
def calcular_preco_com_desconto(preco, percentual_desconto):
    desconto = (preco * percentual_desconto) / 100
    preco_final = preco - desconto
    return preco_final

try:
    preco_produto = float(input("Digite o preço do produto: R$ "))
    percentual = float(input("Digite o percentual de desconto (%): "))
    
    if preco_produto < 0 or percentual < 0:
        raise ValueError("Os valores não podem ser negativos.")
    
    preco_com_desconto = calcular_preco_com_desconto(preco_produto, percentual)
    
    print(f"Preço final após desconto: R$ {preco_com_desconto:.2f}")
except ValueError as ve:
    print(f"Entrada inválida: {ve}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
