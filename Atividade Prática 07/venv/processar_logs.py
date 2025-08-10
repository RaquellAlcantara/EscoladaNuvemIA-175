'''
1- Leia um arquivo que contenha dados de log de treinamento de modelos de Machine.
'''

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execução'].mean()
    desvio_padrao_tempo = df['tempo_execução'].std()
    print(f"Média do tempo de execução: {media_tempo:.2f} segundos.")
    print

nome_arquivo = input("Digite o nome do arquivo de log")
processar_logs_treinamento(nome_arquivo)