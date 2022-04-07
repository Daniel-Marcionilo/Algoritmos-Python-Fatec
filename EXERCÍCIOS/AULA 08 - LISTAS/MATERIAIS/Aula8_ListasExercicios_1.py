# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 1 das Tarefas da Aula 9

L = []
cont = 0
while cont < 10:
    X = int(input("Digite o elemento {} da lista: ".format(cont)))
    L.append(X)
    cont = cont + 1

print("\nElementos da lista")
for X in L:
    print(X)

print("\n\nFim do Programa")



