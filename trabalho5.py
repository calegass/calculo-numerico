"""
Matheus Calegari
Pedro Henrique Guerra

Trabalho 5
Crie um programa no PYTHON para encontrar raízes
pelo método da secante em relação a função
com aproximação inicial – 8 e fator de perturbação
igual a 10– 6.

f(x) = sin(x/2) * log10(-10x)
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# definindo a função
def f(x):
    return np.sin(x / 2) * np.log10(-10 * x)


# método da secante
def metodo_secante(f, x0, x1, tol, max_iter):
    iter_count = 0
    while iter_count < max_iter:  # enquanto o número de iterações for menor que o máximo
        iter_count += 1
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))  # calculando o próximo valor de x
        if abs(x2 - x1) < tol:  # se a diferença entre os valores de x for menor que a tolerância
            return x2, iter_count  # retorna o valor de x e o número de iterações
        x0 = x1
        x1 = x2
    print("O método da secante não convergiu após", max_iter, "iterações.")
    return None, max_iter


# Aproximação inicial
x0 = -8
x1 = -8 + 1e-6  # Perturbação de 10^-6
# Fator de perturbação
tolerance = 1e-6
# Número máximo de iterações
max_iterations = 100

# Chamando a função
raiz, iterations = metodo_secante(f, x0, x1, tolerance, max_iterations)

if raiz is not None:
    print("Raiz encontrada:", raiz)
    print("Número de iterações:", iterations)
else:
    print("Raiz não encontrada com a tolerância especificada.")

# Plotando o gráfico
x_values = np.linspace(-10, 10)
plt.plot(x_values, f(x_values), label='f(x)')
plt.scatter(raiz, f(raiz), color='red', label='Raiz encontrada')
plt.title('Gráfico da função f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
