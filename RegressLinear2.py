import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Aprendendo a aplicar com scikit-learn (Regressão Linear - forma automática).

# É preciso que os valores aqui estejam dentros de matrizes 2Dimensões (S) na entrada. 
x = np.array([[1], [2], [3]])
y = np.array([2, 4, 5])

# Instanciando a classe LinearRegression em modelo.
modelo = LinearRegression()

# Aplicando o algoritmo da Regressão Linear. 
modelo.fit(x,y)

plt.scatter(x,y,color = "blue", s = 60, label = "Dados reais")
plt.plot(x,modelo.predict(x), color = "red", label = "Reta ajustada")

# Zip funciona para combinar iteráveis em paralelo criando pares correspondentes. 
for y,yi,x in zip(y,modelo.predict(x),x):
    plt.vlines(x,y,yi,color = "gray", linestyles="dashed")

plt.title("Regressão Linear")
plt.show()


