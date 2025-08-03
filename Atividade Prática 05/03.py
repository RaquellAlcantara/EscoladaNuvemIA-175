'''
3- Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
'''

def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

while True:
    try:
        preco_original = float(input("Digite o preço do produto (exemplo: 250.75): "))
        desconto = float(input("Digite o percentual de desconto (exemplo: 10): "))
        
        if preco_original < 0 or desconto < 0:
            print("Preço e desconto devem ser valores positivos.")
            continue

        preco_final = calcular_desconto(preco_original, desconto)
        print(f"Preço final após desconto: R$ {preco_final:.2f}")
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
