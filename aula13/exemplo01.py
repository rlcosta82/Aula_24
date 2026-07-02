# pip install polars
import pandas as pd
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo


ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')

    # Pandas: 0:00:19.475724
    # df_bolsa_familia = pd.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1' )

    # Polars: 0:00:08.481386
    df_bolsa_familia = pl.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1' )

    print(df_bolsa_familia)

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')