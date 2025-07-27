#2- Calculadora de Desconto 

#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#Nome do produto: "Camiseta"

#Preço original: R$ 50.00

#Porcentagem de desconto: 20% 
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta",
preco_original = 50.00,
p_desconto  = 20,

v_desconto = (preco_original * p_desconto) / 100,
p_final = preco_original - v_desconto,

print("Produto:", nome_produto),
print("Preço original: R$ ",preco_original),
print("Desconto:", p_desconto),
print("Valor do desconto: R$ ", v_desconto),
print("Preço final com desconto: R$ ", p_final)
