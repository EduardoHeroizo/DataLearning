import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

diabetes = load_diabetes()

modelo = LinearRegression()

# Esse Dataset está armazenado em dict.
modelo.fit(diabetes["data"],diabetes["target"])

# Estamos utilizando todas as features, se quisessemos comparar apenas com uma (slicing + reshape(-1,1))
# Fit aceita apenas modelos bidimensionais.
y = diabetes["target"]
y_predict = modelo.predict(diabetes["data"])

# O que realmente faz a comparação entre y e ypredict(Aplicado ao modelo) é o scatter.
plt.scatter(modelo.predict(diabetes["data"]),diabetes["target"], color = "blue", s = 30, label = "Dados reais")
# Aqui é só uma referência visual.

plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label="Linha perfeita: y = y_pred")
plt.legend()
plt.show()

