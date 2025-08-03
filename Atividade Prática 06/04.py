'''

'''

import requests

def obter_cotacao():
    url = f"https://economia.awesoneapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máxima: R$ {float(cotacao['bid']):.2f}
        Mínima: R$ {float(cotacao['bid']):.2f}
        Data/Hora:
        """
    except requests.exceptions.RequestException as  e:
        return f"Erro ao obter usuário: {e}"
    except KeyError:
        return f""


def main():
    moeda = input("Digite o código da moeda para cotação (ex. USD, EUR, GBP)").upper()
    print("\nObtendo cotação")
    resultado = obter_cotacao(moeda)
    print(resultado)

if __name__== "__main__":
    main()
