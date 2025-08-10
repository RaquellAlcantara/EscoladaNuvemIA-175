'''
2- Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
'''

import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            for linha in dados:
                escritor.writerow(linha)
        print(f"Dados salvos com sucesso em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

dados = [
    ["Ana", 30, "Rio de Janeiro"],
    ["Pedro", 22, "São Paulo"],
    ["Maria", 25, "Salvador"]
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo csv (exemplo: pessoas.csv): ").strip()
    escrever_csv(nome_arquivo, dados)
