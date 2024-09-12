"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 12
Crie um programa no Python para ajustar um polinômio de
segundo grau aos dados da Tabela abaixo. Exiba os
coeficientes da equação e o coeficiente de r2.

xi = [0, 1, 2, 3, 4, 5]
yi = [3.1, 6.9, 13.6, 28.2, 42.9, 61.1]
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função usada
def regressao_polinomial(x, y, grau=2):
    n = len(x)
    A = np.zeros((grau + 1, grau + 1))
    B = np.zeros(grau + 1)

    for i in range(grau + 1):
        for j in range(grau + 1):
            A[i, j] = np.sum(x ** (i + j))
        B[i] = np.sum(y * x ** i)

    coeficientes = np.linalg.solve(A, B)
    y_pred = np.polyval(coeficientes[::-1], x)
    r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2)
    return coeficientes, r2


# Dados
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([3.1, 6.9, 13.6, 28.2, 42.9, 61.1])

# Regressão
coeficientes, r2 = regressao_polinomial(x, y)

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Dados")
plt.plot(x, np.polyval(coeficientes[::-1], x), color="red", label="Polinômio de segundo grau")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão Polinomial")
plt.legend()
plt.grid(True)
plt.show()

print(f"Os coeficientes do polinômio de segundo grau são {coeficientes}.")
print(f"O coeficiente r2 é {r2}.")
