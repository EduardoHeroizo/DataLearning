import pandas as pd           
import numpy as np            
import matplotlib.pyplot as plt 
import os                    

# Montando o caminho da pasta onde estão os arquivos CSV.
pasta_csv = os.path.join(os.getcwd(), "CsvArquivos")

# Montando o caminho completo até o arquivo de vendas.
arquivo_vendas = os.path.join(pasta_csv, "vendas.csv")

# Exibindo o diretório atual e o arquivo que será lido (para conferência).
print("Diretório atual:", os.getcwd())
print("Lendo arquivo:", arquivo_vendas)

# Lendo o arquivo CSV para dentro de um DataFrame do pandas.
df = pd.read_csv(arquivo_vendas)

# Exibindo as primeiras linhas do DataFrame para entender sua estrutura.
print("\nPrimeiras linhas:")
print(df.head())

# Exibe informações gerais do DataFrame:
# quantidade de valores não nulos, tipo de dados, memória usada, etc.
print("\nInformações do DataFrame:")
print(df.info())

# Mostra um resumo estatístico da coluna 'Vendas':
# count (quantidade), mean (média), min, max, std (desvio padrão) etc.
print("\nResumo estatístico da coluna 'Vendas':")
print(df["Vendas"].describe())

# Mostra a contagem de valores ausentes (NaN) em cada coluna.
print("\nContagem de valores NaN por coluna:")
print(df.isna().sum())

# Calcula a média das vendas para substituir valores NaN.
media_vendas = df["Vendas"].mean()

# Substitui os valores NaN da coluna 'Vendas' pela média calculada.
df["Vendas"] = df["Vendas"].fillna(media_vendas)

# Substitui valores NaN de 'Clientes' por 0 e converte para inteiro.
df["Clientes"] = df["Clientes"].fillna(0).astype(int)

# Cria uma nova coluna 'Receita' multiplicando Vendas por Clientes.
df["Receita"] = df["Vendas"] * df["Clientes"]

# Cria uma coluna 'Categoria' que classifica as vendas:
# se Vendas > 150 -> 'Alta', senão -> 'Baixa'.
df["Categoria"] = np.where(df["Vendas"] > 150, "Alta", "Baixa")

# Agrupa por cidade e soma as colunas numéricas selecionadas.
resumo_cidade = df.groupby("Cidade")[["Vendas", "Clientes", "Receita"]].sum()

# Agrupa por produto e calcula a média das vendas.
media_produto = df.groupby("Produto")["Vendas"].mean()

# Exibe o resumo por cidade.
print("\nResumo por cidade:")
print(resumo_cidade)

# Exibe a média de vendas por produto.
print("\nMédia de vendas por produto:")
print(media_produto)

# Salva o resumo por cidade.
resumo_cidade.to_csv(os.path.join(pasta_csv, "resumo_cidade.csv"), index=True, encoding="utf-8")

# Salva a média de vendas por produto.
media_produto.to_csv(os.path.join(pasta_csv, "media_produto.csv"), index=True, encoding="utf-8")

# Salva o DataFrame completo e tratado com caminho aplicado.
df.to_csv(os.path.join(pasta_csv, "vendas_tratado.csv"), index=False, encoding="utf-8")

# Gráfico de barras com o total de clientes por cidade.
resumo_cidade["Clientes"].plot(kind="bar", title="Vendas por cidade")
plt.ylabel("Vendas")
plt.tight_layout()   # Ajusta o layout para evitar sobreposição dos elementos.
plt.show()

# Gráfico de pizza mostrando a média de vendas por produto; é preciso colocar figure e show novamente para novo gráfico.
plt.figure(figsize=(5,5)) # Autopct é a porcentagem automática, estamos aplicando 1.1f.
media_produto.plot(kind="pie", autopct="%1.1f%%", title="Média de Vendas por Produto") 
# Retirando, apenas não aparece valores na pizza. 
plt.tight_layout() 
plt.show()

# Exibe o caminho final onde os CSVs foram salvos.
print("\nArquivos csv salvos em:", pasta_csv)