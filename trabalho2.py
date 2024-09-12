"""
Matheus Calegari
Pedro Henrique Guerra

Trabalho 2
Crie uma função no Scilab para estimar raízes pelo
método da bisseção. O programa deverá permitir a
escolha dos limites inferior e superior do intervalo de
busca e o erro tolerado para conclusão do
treinamento. Use essa função para identificar os
subintervalos nos quais ocorre mudança de sinal
dentro do intervalo [4,11] para a função abaixo. Envie
o trabalho para o e-mail josericardo@iftm.edu.br.

f(x) = np.log10(x) + (3 * np.sin(x/2))
"""


import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


# definindo os limites do intervalo e o número de subintervalos
inf = 4
sup = 11
n_subintervalos = 100
tolerancia = 1e-4


def f(value):
    return np.log10(value) + (3 * np.sin(value / 2))


def bissecao(func, inferior, superior, tolerancia):
    if np.sign(func(inferior)) == np.sign(func(superior)):  # se a função não muda de sinal
        raise ValueError("A função não muda de sinal no intervalo dado.")

    while (superior - inferior) / 2 > tolerancia:  # enquanto a diferença entre os limites for maior que a tolerância
        meio = (inferior + superior) / 2
        if func(meio) == 0:
            return meio  # se o valor do meio for a raiz
        elif np.sign(func(meio)) == np.sign(func(inferior)):
            inferior = meio
        else:
            superior = meio
    return (inferior + superior) / 2  # retorna o valor do meio


def subintervalos_bissecao(f, inferior, superior):
    subintervalos = []
    raizes = []

    # por enquanto método de busca incremental
    tam_subintervalos = (superior - inferior) / n_subintervalos
    intervalo_atual = inferior
    while intervalo_atual < superior:
        if np.sign(f(intervalo_atual)) != np.sign(f(intervalo_atual + tam_subintervalos)):
            raiz = bissecao(f, intervalo_atual, intervalo_atual + tam_subintervalos, tolerancia)  # chamando a função
            raizes.append(raiz)  # adicionando a raiz
            subintervalos.append((intervalo_atual, intervalo_atual + tam_subintervalos))
        intervalo_atual += tam_subintervalos
    return subintervalos, raizes


intervalos, raizes = subintervalos_bissecao(f, inf, sup)  # chamando a função
print("Intervalos nos quais ocorre mudança de sinal:")
for intervalo in intervalos:
    print(intervalo)
print("\nRaízes encontradas usando o método da bisseção:")
print(raizes)

x = np.linspace(inf, sup)
y = f(x)

# plotando o gráfico
plt.plot(x, y, label='f(x)')
plt.scatter(raizes, [f(r) for r in raizes], color='red', label='Raízes encontradas')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Bisseção')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
