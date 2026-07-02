# pip install polars
import pandas as pd
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo


ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')

    # Dataframe para controle (principal)
    df_bolsa_familia = None

    lista_arquivos = ['202601_NovoBolsaFamilia.csv', '202602_NovoBolsaFamilia.csv']



    for nome in lista_arquivos:
        print(f'Processando o arquivo {nome}')

        # Pandas: 0:00:56.241461
        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=';', encoding='iso-8859-1' )

        # Polars: 0:00:11.396078
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=';', encoding='iso-8859-1' )

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df
        
    print(df_bolsa_familia)

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')