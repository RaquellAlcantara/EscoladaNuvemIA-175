'''


'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status
        dados = response.json()
        if"erro"in dados:
            return 'CEP nãao encontrado'
        return f"""
        CEP: {dados['cep']}
        Logradouro
        """

cep =input()

