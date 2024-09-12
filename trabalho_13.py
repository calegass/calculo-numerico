"""
Matheus Calegari Moizinho
Pedro Henrique Guerra

Trabalho 13
Crie um programa no Python para obter um modelo de
regressão linear múltipla para os dados da Tabela abaixo.
Exiba os coeficientes do modelo.

x1i = [0, 2, 2.5, 1, 4, 7]
x2i = [0, 1, 2, 3, 6, 2]
y = [6, 11, 9, 1, 3, 27]
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# Função para regressão linear múltipla
def regressao_linear_multipla(X, y):
    # Adiciona a coluna de 1s para a intercepção
    X = np.column_stack((np.ones(X.shape[0]), X))

    XTX = np.dot(X.T, X)  # Multiplicação de matrizes
    XTY = np.dot(X.T, y)  # Multiplicação de matrizes
    beta_hat = np.linalg.solve(XTX, XTY)  # Resolve o sistema de equações lineares[

    return beta_hat


# Dados
x1 = np.array([0, 2, 2.5, 1, 4, 7])
x2 = np.array([0, 1, 2, 3, 6, 2])
X = np.column_stack((x1, x2))  # Matriz de variáveis independentes
y = np.array([6, 11, 9, 1, 3, 27])

# Calcula os coeficientes usando a função
beta_hat = regressao_linear_multipla(X, y)

# Exibe os coeficientes do modelo
print("Os coeficientes do modelo de regressão linear múltipla são:")
print("Intercepção (β0):", beta_hat[0])
print("Coeficiente para x1 (β1):", beta_hat[1])
print("Coeficiente para x2 (β2):", beta_hat[2])

# Plotagem 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plano de regressão
x1_grid, x2_grid = np.meshgrid(np.linspace(min(x1), max(x1), 10), np.linspace(min(x2), max(x2), 10))
y_pred_plane = beta_hat[0] + beta_hat[1] * x1_grid + beta_hat[2] * x2_grid
ax.plot_surface(x1_grid, x2_grid, y_pred_plane, alpha=0.5, color='r')

ax.scatter(x1, x2, y, label="Dados")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
plt.title("Regressão Linear Múltipla")
plt.legend()
plt.grid(True)

plt.show()
