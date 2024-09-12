"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 17

Crie um programa no Python para calcular a integral da
função
f(x) = 6 + 3cos(x)
usando a regra do trapézio. O programa deverá permitir que o
usuário escolha o intervalo de integração, a quantidade de
intervalos e apresentar o resultado da integral.
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def f(x):
    return 6 + 3 * np.cos(x)


def trapezio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h / 2 * (y[0] + 2 * np.sum(y[1:n]) + y[n])


a = float(input("Digite o limite inferior do intervalo de integração: "))
b = float(input("Digite o limite superior do intervalo de integração: "))

n = int(input("Digite a quantidade de intervalos: "))
integral = trapezio(f, a, b, n)

print(f"A integral da função f(x) = 6 + 3cos(x) no intervalo [{a}, {b}] é aproximadamente {integral}.")

# Gráfico
x = np.linspace(a, b, 100)
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label="f(x) = 6 + 3cos(x)")
plt.fill_between(x, f(x), alpha=0.2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regra do Trapézio")
plt.legend()
plt.grid(True)
plt.show()
