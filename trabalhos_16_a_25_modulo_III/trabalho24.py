"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 24

Crie um programa no Python para resolver o problema de
valor inicial
dy/dt = yt^3 - 1.5y
y(0) = 1
usando o método de Runge-Kutta de quarta ordem clássico. O
programa deverá permitir a escolha de h. Verifique os
resultados com h = 0,25 e o intervalo para t de 0 a 4.
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def f(t, y):
    return y * t**3 - 1.5 * y


def rk4(f, a, b, y0, h):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(t[i + 1], y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y


a = 0
b = 4
y0 = 1
h = 0.25

t, y = rk4(f, a, b, y0, h)

np.set_printoptions(precision=2)
print("t:", t)
print("y:", y)

# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(t, y, label="y(t)")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Método de Runge-Kutta de 4ª Ordem")
plt.legend()
plt.grid(True)
plt.show()
