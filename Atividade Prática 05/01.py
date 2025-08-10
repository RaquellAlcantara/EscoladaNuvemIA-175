'''
1- Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada.
'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    print(f"Valor da conta: R$ {valor_conta:.2f}")
    print(f"Porcentagem da gorjeta desejada: {porcentagem_gorjeta}%")

    gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    print(f"Valor calculado da gorjeta: R$ {gorjeta:.2f}")

    total = valor_conta + gorjeta
    print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")

    return gorjeta, total

valor_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta necessária: "))

