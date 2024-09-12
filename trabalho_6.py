"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 6
Crie um programa que utiliza a razão áurea
para maximizar a função
f(x) = -x^4 + 2x^3 - 2x + 6
Considerando o intervalo de busca inicial de
[– 6, 6]. Estabeleça como critério de parada a
precisão de 10–8 para o erro estimado.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função usada
def f(x):
    return -x**4 + 2*x**3 - 2*x + 6


# Função razão áurea
def razao_aurea(f, a, b, tol=1e-8, max_iter=1000):
    phi = (1 + np.sqrt(5)) / 2
    # Pontos de amostra
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    f1 = f(x1)
    f2 = f(x2)

    # Iterações
    for _ in range(max_iter):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / phi
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / phi
            f2 = f(x2)
        if abs(b - a) < tol:
            break
    else:
        print("O método não convergiu.")
    return (a + b) / 2


# Limites
a, b = -6, 6

# Maximizando a função invertida
max_x = razao_aurea(lambda x: -f(x), a, b)  # Invertendo a função para achar o mínimo
max_y = f(max_x)  # Invertendo o valor do mínimo para achar o máximo

print(f"Máximo encontrado: x = {max_x}, f(x) = {max_y}")

# Plot
x = np.linspace(-6, 6, 1000)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.scatter(max_x, max_y, color="red", label="Máximo")
plt.title("Razão Áurea")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
