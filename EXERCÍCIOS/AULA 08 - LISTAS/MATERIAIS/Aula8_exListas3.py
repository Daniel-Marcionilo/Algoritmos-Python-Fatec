# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 3 do final do PDF da Aula 8

L = []
cont = 0
while cont < 10:
    X = int(input("Digite um valor: "))
    L.append(X)
    cont = cont + 1

print("\nExibição da lista em ordem inversa")
print("  exibição usando comando while")
i = 9
while i >= 0:
    print(L[i])
    i = i - 1
    
print("\n  exibição usando comando for")
L.reverse()
for a in L:
    print(a)


print("\n\nFim do Programa")



