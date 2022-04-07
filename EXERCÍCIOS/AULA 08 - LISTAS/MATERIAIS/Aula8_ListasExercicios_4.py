# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 4 das Tarefas da Aula 9

from random import randint

N = int(input("Digite N: "))
while N < 0 or N > 50:
    print("  {} inválido".format(N))
    N = int(input("Digite N: "))

L = []
i = 0
while i < N:
    valor = randint(0, 1000)
    L.append(valor)
    i = i + 1

print(L)

print("\n\nFim do Programa")



