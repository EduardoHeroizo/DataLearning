import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from openai import OpenAI

arquivo = input("Digite o caminho do arquivo: ").strip()

try:
    df = pd.read_csv(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    sys.exit()

print("Primeiras linhas do dataset:")
print(df.head())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna("Desconhecido")

variavel_alvo = input("Digite o nome da variável alvo: ").strip()

if variavel_alvo not in df.columns:
    print(f"Coluna '{variavel_alvo}' não existe no dataset.")
    print("Colunas disponíveis:", list(df.columns))
    sys.exit()

if not pd.api.types.is_numeric_dtype(df[variavel_alvo]):
    print(f"A variável alvo '{variavel_alvo}' não é numérica. LinearRegression precisa de alvo numérico.")
    sys.exit()

colunas_preditoras = [
    col for col in df.select_dtypes(include="number").columns
    if col != variavel_alvo
]

if len(colunas_preditoras) == 0:
    print("Não há colunas preditoras numéricas (diferentes da variável alvo).")
    sys.exit()

if len(colunas_preditoras) == 1:
    print("Regressão Linear Simples")
else:
    print("Regressão Linear Múltipla")

X = df[colunas_preditoras]
y = df[variavel_alvo]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_predict_test = modelo.predict(X_test)
y_predict_train = modelo.predict(X_train)

r2_treino = r2_score(y_train, y_predict_train)
r2_teste = r2_score(y_test, y_predict_test)

intercepto = float(modelo.intercept_)
coef = [float(c) for c in modelo.coef_]

contexto = f"""
R² treino: {r2_treino:.4f}
R² teste: {r2_teste:.4f}

Variável alvo: {variavel_alvo}
Colunas preditoras: {colunas_preditoras}

Intercepto: {intercepto}

Coeficientes (na mesma ordem das colunas preditoras):
{list(zip(colunas_preditoras, coef))}
"""

client = OpenAI()

instructions = (
    "Você é um analista de dados. "
    "Use APENAS as informações fornecidas. "
    "Não invente números nem causalidade. "
    "Se algo não der para afirmar, diga que não dá."
)

prompt = f"""
Explique:
1) O que os valores de R² indicam
2) Se há overfitting, underfitting ou bom ajuste
3) O significado dos coeficientes
4) Gere 3 insights em linguagem simples

Contexto:
{contexto}
""".strip()

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions=instructions,
    input=prompt
)

print(response.output_text)