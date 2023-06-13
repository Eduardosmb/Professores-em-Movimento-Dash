import pandas as pd

# Carregar os dados das planilhas
df_violencia = pd.read_excel('violencia_por_bairro.xlsx')
df_resultados = pd.read_excel('resultados_finais_idh_ird.xlsx')

# Realizar a junção dos dados com base na coluna "Bairro"
df_merged = pd.merge(df_resultados, df_violencia, on='Bairro')

# Selecionar apenas as colunas desejadas
df_new = df_merged[['IRD', 'Mortes']]

# Salvar a nova planilha em um arquivo
df_new.to_excel('nova_planilha.xlsx', index=False)
