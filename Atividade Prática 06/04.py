'''
4- Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
'''
import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Cotação {moeda} para BRL:")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Máximo: R$ {info['high']}")
            print(f"Mínimo: R$ {info['low']}")
            print(f"Data/Hora da última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada na API.")
    else:
        print("Erro ao consultar a cotação.")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda)
