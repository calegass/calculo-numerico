"""
Matheus Calegari
Pedro Henrique Guerra

Trabalho 4
Crie um programa no PYTHON para encontrar raízes
pelo método de iteração de ponto fixo simples da
função com aproximação inicial 2.

f(x) = 2x^3 - 11.7x^2 + 17.7x - 5
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# inicializando as variáveis
initial_approach = 2
error = 0.0001
max_iterations = 1000


# definindo a função e as funções g
def f(x):
    return 2 * x ** 3 - 11.7 * x ** 2 + 17.7 * x - 5


def g1(x):
    return (2 * x ** 3 - 11.7 * x ** 2 - 5) / (-17.7)


def g2(x):
    return np.sqrt((2 * x ** 3 + 17.7 * x - 5) / 11.7)


def g3(x):
    return ((-11.7 * x ** 2 + 17.7 * x - 5) / -2) ** (1 / 3)


# método de iteração de ponto fixo
def ponto_fixo(g, x0, tol, max_iter):
    iter_count = 0
    x_values = [x0]
    while iter_count < max_iter:  # enquanto o número de iterações for menor que o máximo
        x1 = g(x0)  # calculando o próximo valor de x
        x_values.append(x1)  # adicionando o valor de x à lista
        if abs(x1 - x0) < tol:  # se a diferença entre os valores de x for menor que a tolerância
            print("Convergência alcançada após", iter_count, "iterações.")
            return x1, x_values
        x0 = x1
        iter_count += 1
    print("O método de iteração de ponto fixo não convergiu após", max_iter, "iterações.")
    return None, x_values


# chamando a função
for g_func in [g1, g2, g3]:
    print("\nUsando função:", g_func.__name__)
    raiz, x_values = ponto_fixo(g_func, initial_approach, error, max_iterations)
    if raiz is not None:  # se a raiz foi encontrada
        print("Raiz encontrada:", raiz)
        plt.plot(range(len(x_values)), x_values, marker='o', label=g_func.__name__)  # adicionando os valores de x
    else:
        print("Raiz não encontrada com a tolerância especificada.")

# plotando o gráfico
plt.title("Convergência do Método de Iteração de Ponto Fixo")
plt.xlabel("Iterações")
plt.ylabel("x")
plt.legend()
plt.grid(True)
plt.show()
