# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 3 das Tarefas da Aula 9

N = int(input("Digite N: "))
while N < 0 or N > 50:
    print("  {} inválido".format(N))
    N = int(input("Digite N: "))
    

L = []
cont = 0
while cont < N:
    X = float(input("Digite o elemento {} da lista: ".format(cont)))
    L.append(X)
    cont = cont + 1

print("\nElementos da lista")
for X in L:
    print(X)

print("\n\nFim do Programa")



