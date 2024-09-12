"""
Matheus Calegari
Pedro Henrique Guerra

Trabalho 1
Crie uma função no Scilab para estimar raízes pelo
método de busca incremental. O programa deverá
permitir a escolha dos limites inferior e superior do
intervalo de busca e o número de subintervalos. Use
essa função para identificar os subintervalos nos
quais ocorre mudança de sinal dentro do intervalo
[4,11] para a função abaixo. Envie o trabalho para o
e-mail josericardo@iftm.edu.br.

f(x) = np.log10(x) + (3 * np.sin(x / 2))
"""


import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# definindo os limites do intervalo e o número de subintervalos
inf = 4
sup = 11
n_subintervalos = 100

# incializando as listas
subintervalos = []
x = []
y = []


def f(value):
    return np.log10(value) + (3 * np.sin(value / 2))  # função dada


def busca_incremental(func, inferior, superior):
    tam_subintervalo = (superior - inferior) / n_subintervalos  # tamanho do subintervalo
    intervalo_atual = inferior  # inicializando o intervalo atual
    while intervalo_atual < superior:
        x.append(intervalo_atual)  # adicionando o valor de x
        y.append(func(intervalo_atual))  # adicionando o valor de f(x)
        if np.sign(func(intervalo_atual)) != np.sign(func(intervalo_atual + tam_subintervalo)):  # se houver mudança
            # de sinal
            subintervalos.append((intervalo_atual, intervalo_atual + tam_subintervalo))  # adiciona o subintervalo
            print(subintervalos[-1])
        intervalo_atual += tam_subintervalo  # atualiza o intervalo atual


print("Subintervalos nos quais ocorre mudança de sinal:")
busca_incremental(f, inf, sup)  # chamando a função

# plotando o gráfico
plt.plot(x, y, label='f(x)')
for subintervalo in subintervalos:
    plt.axvline(subintervalo[0], color='red', linestyle='--')
plt.title('Busca Incremental')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
