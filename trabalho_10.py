"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 10
Use a regressão por mínimos quadrados para ajustar
uma reta aos dados da tabela abaixo.

x = [6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]
y = [29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3]

Construa um programa no Python que determine:
a) O gráfico dos pontos amostrados, juntamente com a reta
obtida na regressão.
b) Os coeficientes a0 e a1 da regressão linear.
c) O coeficiente r2 para o modelo.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função usada
def regressao_minimos_quadrados(x, y):
    n = len(x)
    a1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)  # Coeficiente angular
    a0 = np.mean(y) - a1 * np.mean(x)  # Coeficiente linear
    r2 = 1 - np.sum((y - a0 - a1 * x)**2) / np.sum((y - np.mean(y))**2)  # Coeficiente r2
    return a0, a1, r2  # Retorna os coeficientes


# Dados
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])

# Regressão
a0, a1, r2 = regressao_minimos_quadrados(x, y)

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Dados")
plt.plot(x, a0 + a1 * x, color="red", label="Reta de regressão")
plt.xlabel("x")
plt.ylabel("y")
plt.title("a) Regressão por Mínimos Quadrados")
plt.legend()
plt.grid(True)
plt.show()

print(f"b) Os coeficientes da regressão são a0 = {a0} e a1 = {a1}.")
print(f"c) O coeficiente r2 é {r2}.")
