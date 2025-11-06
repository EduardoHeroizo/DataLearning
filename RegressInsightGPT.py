import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
import sys  

arquivo = input("Digite o caminho do arquivo")

try:
    df = pd.read_csv(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    sys.exit()
    

print("Primeiras linhas do dataset:")
print(df.head())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Desconhecido")

variavel_alvo = input("Digite o nome da variável alvo: ")
colunas_preditoras = [col for col in df.select_dtypes(include="number").columns if col != variavel_alvo]

if len(colunas_preditoras) == 0: 
    print("Não há colunas preditoras")
    exit()

X = df[colunas_preditoras]
Y = df[variavel_alvo]

modelo = LinearRegression()
modelo.fit(X,Y)

if len(colunas_preditoras) == 1: 
    # Regressão linear simples.  
    print() 


