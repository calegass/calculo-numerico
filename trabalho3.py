"""
Matheus Calegari
Pedro Henrique Guerra

Trabalho 3
Crie um programa no Scilab para determinação de
raízes pelo método da falsa posição e em seguida
resolva o mesmo problema abordado no trabalho 2.
Envie o trabalho para o e-mail
josericardo@iftm.edu.br.

f(x) = np.log10(x) + (3 * np.sin(x/2))
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="darkgrid")


def f(value):
    return np.log10(value) + (3 * np.sin(value / 2))  # função dada


# método da falsa posição
def falsa_posicao(f, sub_inferior, sub_superior, erro):
    if np.sign(f(sub_superior)) == np.sign(f(sub_inferior)):  # se a função não muda de sinal
        print("A função não muda de sinal nos pontos dados.")
        return None

    while (sub_superior - sub_inferior) >= erro:
        ponto_medio = (sub_inferior * f(sub_superior) - sub_superior * f(sub_inferior)) / (
                    f(sub_superior) - f(sub_inferior))  # calculando o ponto médio

        if abs(f(ponto_medio)) < erro:  # se o módulo do ponto médio for menor que a tolerância
            return ponto_medio

        if f(ponto_medio) * f(sub_inferior) < 0:
            sub_superior = ponto_medio
        else:
            sub_inferior = ponto_medio

    return (sub_inferior + sub_superior) / 2  # retorna o valor do ponto médio


def encontrar_raizes(f, intervalos, erro):
    raizes = []
    for intervalo in intervalos:
        sub_inferior, sub_superior = intervalo
        raiz = falsa_posicao(f, sub_inferior, sub_superior, erro)
        if raiz is not None:
            raizes.append(raiz)
    return raizes  # retorna as raízes encontradas


# aqui é o mesmo método de busca incremental do trabalho 1
inferior = 4
superior = 11
n_subintervalos = 100
erro = 0.0001

tam_subintervalo = (superior - inferior) / n_subintervalos
sub_inferior_atual = inferior
subintervalos = []

while sub_inferior_atual < superior:
    if np.sign(f(sub_inferior_atual)) != np.sign(f(sub_inferior_atual + tam_subintervalo)):
        sub_superior = sub_inferior_atual + tam_subintervalo
        subintervalos.append((sub_inferior_atual, sub_superior))
    sub_inferior_atual += tam_subintervalo

print("Subintervalos nos quais ocorre mudança de sinal:")
for subintervalo in subintervalos:
    print(subintervalo)

# chamando a função
raizes = encontrar_raizes(f, subintervalos, erro)
print("\nRaízes encontradas usando o método da falsa posição:")
for raiz in raizes:
    print(raiz)

# definindo o intervalo de x
x = np.linspace(inferior, superior)

# plotando o gráfico
plt.plot(x, f(x), label='f(x)')
plt.scatter(raizes, [f(r) for r in raizes], color='red', label='Raízes encontradas')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Falsa posição')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)', 'Raízes'])
plt.grid(True)
plt.show()
