"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 15

Crie um programa no Python para determinar os coeficientes
do polinômio interpolador de Lagrange, para uma ordem
qualquer especificada pelo usuário. Use o programa para
determinar:
a) O valor de f(1,5) considerando os dados abaixo:
x -1 0 1 2
f(x) 17 14 10 40
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def lagrange(x, y, r):
    n = len(x)
    soma = 0
    for i in range(n):
        prod = y[i]
        for j in range(n):
            if i != j:
                prod *= (r - x[j]) / (x[i] - x[j])
        soma += prod
    return soma


x = np.array([-1, 0, 1, 2])
y = np.array([17, 14, 10, 40])

print("O valor de f(1.5) é: ", lagrange(x, y, 1.5))

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Dados")
plt.plot(x, lagrange(x, y, x), color="red", label="Polinômio interpolador de Lagrange")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolação de Lagrange")
plt.legend()
plt.grid(True)
plt.show()
