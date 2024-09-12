"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 14

Crie um programa no Python para determinar os coeficientes
do polinômio interpolador de Newton, para uma ordem
qualquer especificada pelo usuário. Use o programa para
determinar:
a) Os coeficientes do polinômio interpolador de Newton de 3ª
ordem dos seguintes dados:
x 8 9 10 11 12 13
f(x) 400 900 1500 2250 3200 4400
b) Estime f(11,8).
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def coeficientes(x, y):
    n = len(x)
    coef = np.zeros(n)
    for i in range(n):
        coef[i] = y[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = float(coef[i] - coef[i-1]) / float(x[i] - x[i-j])
    return coef


def avalia(coef, x, r):
    n = len(coef) - 1
    temp = coef[n]
    for i in range(n-1, -1, -1):
        temp = temp * (r - x[i]) + coef[i]
    return temp


x = np.array([8, 9, 10, 11, 12, 13])

y = np.array([400, 900, 1500, 2250, 3200, 4400])

coef = coeficientes(x, y)

print("Coeficientes do polinômio interpolador de Newton de 3ª ordem: ", coef)

print("Estimativa de f(11.8): ", avalia(coef, x, 11.8))

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Dados")
plt.plot(x, avalia(coef, x, x), color="red", label="Polinômio interpolador de Newton")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolação de Newton")
plt.legend()
plt.grid(True)
plt.show()
