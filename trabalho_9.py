"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 9
Crie um programa que utiliza o método de Gauss-
Seidel para resolver o sistema:
6x + 2y + z - w = 2
- 2x + 7y - z + w = 1/2
- x + y + 8z + w = 2
2x + 2y + z + 9w = 1

Utilize como aproximação inicial a quádrupla
ordenada (0,0,0,0) e como tolerância ε = 0,02.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função usada
def gauss_seidel(A, b, x0, tol=0.02, max_iter=1000):
    D = np.diag(A)  # Diagonal da matriz A
    U = np.triu(A, 1)  # Triangular superior
    L = np.tril(A, -1)  # Triangular inferior

    print(f"Iteração 0: x = {round(x0[0], 6)}, y = {round(x0[1], 6)}, z = {round(x0[2], 6)}")

    # Iterações
    for _ in range(max_iter):
        x = np.linalg.solve(L + np.diag(D), b - np.dot(U, x0))  # Próxima iteração
        if np.linalg.norm(x - x0) < tol:  # Se a norma de x - x0 for menor que a tolerância
            break
        x0 = x

        if _ < 3:
            print(f"Iteração {_ + 1}: x = {round(x[0], 6)}, y = {round(x[1], 6)}, z = {round(x[2], 6)}")

    else:
        print("O método não convergiu.")
    return x  # Retorna a solução


# Matriz A e vetor b
A = np.array([[15, -3, -1], [-3, 18, -6], [-4, -1, 12]])
b = np.array([3800 + 3 * 6, 1200 + 3 * 3, 2350 + 3 * 0])

# Aproximação inicial
x0 = np.array([0, 0, 0])

# Resultado
x = gauss_seidel(A, b, x0)

print(f"A solução do sistema é x = {x}.")
