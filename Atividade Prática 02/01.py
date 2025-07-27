#1- Conversor de Moeda 

#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

#Valor em reais: R$ 100.00

#Taxa do dólar: R$ 5.60

#Taxa do euro: R$ 6.60 

#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

vReais = 100.00
tDolar = 5.60
tEuro = 6.60

vdolar = vReais / tDolar

veuro = vReais / tEuro

print("Valor em reais: R$ ", vReais),
print("Convertido para dólar: US$ ", vdolar),
print ("Convertido para euro: € ", veuro),