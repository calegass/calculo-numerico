"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 11
Sejam os dados da tabela abaixo:

x = [6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]
y = [29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3]

Construa um programa no Python que aplique sobre a regressão
linear as três transformações de dados: exponencial, potência e
saturação. Para cada transformação exiba os seguintes resultados:
a) Coeficientes do modelo.
b) Gráfico na escala original.
c) Gráfico na escala logarítmica para as transformações
exponencial e potência.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função de regressão linear
def regressao_linear(x, y):
    n = len(x)
    a1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x ** 2) - np.sum(x) ** 2)
    a0 = np.mean(y) - a1 * np.mean(x)
    r2 = 1 - np.sum((y - a0 - a1 * x) ** 2) / np.sum((y - np.mean(y)) ** 2)
    return a0, a1, r2


# Dados
x = np.array([6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39])
y = np.array([29, 21, 29, 14, 21, 15, 7, 7, 13, 1, 3])


# Funções de transformação
def exponencial(x):
    return np.exp(x)


def potencia(x):
    return x ** 2


def saturacao(x):
    return 1 / (1 + np.exp(-x))


# Dicionário para armazenar os resultados
resultados = {}

# Loop pelas transformações
for nome, transformacao in [("Exponencial", exponencial), ("Potência", potencia), ("Saturação", saturacao)]:
    x_transformado = transformacao(x)
    a0, a1, r2 = regressao_linear(x_transformado, y)

    # Armazenar resultados
    resultados[nome] = {
        "coeficientes": (a0, a1),
        "r2": r2
    }

    # Gráfico na escala original
    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, a0 + a1 * x_transformado)
    plt.title(f"Regressão {nome} (Escala Original)")
    plt.xlabel("x")
    plt.ylabel("y")

    # Gráfico na escala logarítmica (somente para exponencial e potência)
    if nome in ["Exponencial", "Potência"]:
        plt.figure()
        plt.scatter(x, y)
        plt.plot(x, a0 + a1 * x_transformado)
        plt.xscale("log")
        plt.yscale("log")
        plt.title(f"Regressão {nome} (Escala Logarítmica)")
        plt.xlabel("x (log)")
        plt.ylabel("y (log)")

# Exibir os resultados
for nome, resultado in resultados.items():
    print(f"\n--- Transformação {nome} ---")
    print(f"Coeficientes: {resultado['coeficientes']}")
    print(f"R²: {resultado['r2']:.4f}")

plt.show()
