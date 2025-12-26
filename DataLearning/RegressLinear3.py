import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

diabetes = load_diabetes()
X = diabetes["data"]
y = diabetes["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred_train = modelo.predict(X_train)
y_pred_test = modelo.predict(X_test)

r2_treino = r2_score(y_train, y_pred_train)
r2_teste = r2_score(y_test, y_pred_test)

print("R² treino:", f"{r2_treino:.2f}")
print("R² teste:", f"{r2_teste:.2f}")

plt.scatter(y_pred_test, y_test, s=30, label="Dados de teste")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--",
    label="Linha perfeita: y = y_pred"
)

plt.xlabel("Valor previsto")
plt.ylabel("Valor real")
plt.legend()
plt.show()