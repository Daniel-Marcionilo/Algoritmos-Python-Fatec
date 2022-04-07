# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 2 do final do PDF da Aula 8

L = []
X = 1
while X > 0:
    X = int(input("Digite um valor: "))
    if X > 0:
        L.append(X)

print("\nA lista criada tem os elementos a seguir")
print("  exibição usando comando while")
i = 0
while i < len(L):
    print(L[i])
    i = i + 1
    
print("\n  exibição usando comando for")
for a in L:
    print(a)


print("\n\nFim do Programa")



