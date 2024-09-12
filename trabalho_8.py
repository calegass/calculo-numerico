"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 8
Crie um programa que utiliza o método de Gauss-Jacobi para resolver o sistema:
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
def gauss_jacobi(A, b, x0, tol=0.02, max_iter=1000):
    D = np.diag(A)  # Diagonal da matriz A
    LU = A - np.diagflat(D)  # Matriz A menos a diagonal

    # Iterações
    for _ in range(max_iter):
        x = (b - np.dot(LU, x0)) / D  # Próxima iteração
        if np.linalg.norm(x - x0) < tol:  # Se a norma de x - x0 for menor que a tolerância
            break
        x0 = x
    else:
        print("O método não convergiu.")
    return x  # Retorna a solução


# Matriz A e vetor b
A = np.array([[6, 2, 1, -1], [-2, 7, -1, 1], [-1, 1, 8, 1], [2, 2, 1, 9]])
b = np.array([2, 1/2, 2, 1])

# Aproximação inicial
x0 = np.array([0, 0, 0, 0])

# Resultado
x = gauss_jacobi(A, b, x0)

print(f"A solução do sistema é x = {x}.")

