"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 7
Crie um programa que utiliza a interpolação
quadrática para maximizar a função
f(x) = -x^4 + 2x^3 - 2x + 6
considerando os pontos de busca iniciais – 7,
– 2 e 1. Estabeleça como critério de parada a
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


# Função interpolação quadrática
def interp_quadratica(f, x0, x1, x2, tol=1e-8, max_iter=1000):
    # Iterações
    for _ in range(max_iter):
        # Interpolação
        x3 = (x0 + x1 + x2) / 3
        f3 = f(x3)

        # Encontrar o índice do ponto com o menor valor de f(x)
        idx_min = np.argmin([f(x0), f(x1), f(x2), f3])  # Retorna o índice do menor valor

        # Atualizar os pontos
        if idx_min == 0:  # x0 é o menor
            x0 = x3  # Atualiza x0 para x3
        elif idx_min == 1:
            x1 = x3
        else:
            x2 = x3

        # Verificar a convergência
        if abs(f(x0) - f(x2)) < tol:  # Se a diferença entre f(x0) e f(x2) for menor que a tolerância
            break
    else:
        print("O método não convergiu.")
    return x3  # Retorna o ponto de máximo


# Limites
x0, x1, x2 = -7, -2, 1

# Resultado
x_max = interp_quadratica(f, x0, x1, x2)
print(f"O máximo da função ocorre em x = {x_max} e f(x) = {f(x_max)}.")

# Gráfico
x = np.linspace(-10, 10, 1000)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.scatter(x_max, f(x_max), color='red', label=f'Máximo')
plt.title("Interpolação Quadrática")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
