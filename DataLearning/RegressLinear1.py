import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1, 2, 3])
y = np.array([2, 4, 5])

x_mean = np.mean(x)
y_mean = np.mean(y)

# Esse é o funcionamento da fórmula de covariância e variança.
cov_xy = np.mean((x - x_mean) * (y - y_mean))  # Covariância x,y.
var_x = np.mean((x - x_mean)**2)              # Variância de x.

# Ambas servem para descobrir o valor do coeficiente angular na reta de regressão simples.
a = cov_xy / var_x 

# Para descobrir b é o coeficiente. 
b = y_mean - (a * x_mean)

print("Inclinação (a):",a)
print("Intercepto (b):", b)

# Dessa forma estou obtendo todas as previsões de acordo com a fórmula da regressão linear.
y_pred = a * x + b 
print(y_pred)

plt.scatter(x,y, s = 50, color = "blue", label = "Dados reais")
plt.plot(x,y_pred, color = "red", label = "Reta ajustada")

# Podemos mostrar os erros (linhas verticais).
# Utilizamos o for, pois cada vline representa uma marcação tracedajada(dashed), ymin até ymax. 
for xi, yi, ypi in zip(x, y, y_pred):
    plt.vlines(xi, ypi, yi, colors="gray", linestyles="dashed")

# Nomear os eixos ()
plt.xlabel("Horas de estudo")
plt.ylabel("Nota")

# Preciso usar para executar legendas (label) e gráfico geral.
plt.title("Regressão Linear")
plt.legend()
plt.show()