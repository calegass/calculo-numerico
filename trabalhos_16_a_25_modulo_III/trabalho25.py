"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 25

Um reator de batelada pode ser descrito pelas seguintes
equações:
dC/dt = -e^(-10/T+273)*C
dT/dt = 1000e^(-10/T+273)*C - 20(T - 20)
onde C é a concentração do reagente e T é a temperatura do
reator. A princípio, o reator está a 16ºC e tem uma
concentração do reagente C de 1,0 gmol/L. Encontre a
concentração e a temperatura do reator no tempo t de 0 a 4
usando o método de Runge-Kutta de quarta ordem clássico
para a resolução do sistema de EDOs. Use h = 0,25.
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def f(t, y):
    C, T = y
    dCdt = -np.exp(-10 / (T + 273)) * C
    dTdt = 1000 * np.exp(-10 / (T + 273)) * C - 20 * (T - 20)
    return np.array([dCdt, dTdt])


def rk4(f, a, b, y0, h):
    n = int((b - a) / h)
    t = np.linspace(a, b, n + 1)
    y = np.zeros((n + 1, len(y0)))
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
y0 = np.array([1, 16])
h = 0.25

t, y = rk4(f, a, b, y0, h)

np.set_printoptions(precision=2)
print("t:", t)
print("y:", y)

# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(t, y[:, 0], label="C(t)")
plt.plot(t, y[:, 1], label="T(t)")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Método de Runge-Kutta de 4ª Ordem")
plt.legend()
plt.grid(True)
plt.show()
