# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 4 do final do PDF da Aula 8

print("Leitura da lista A")
A = []
cont = 0
while cont < 10:
    X = int(input("Digite um valor: "))
    A.append(X)
    cont = cont + 1

print("\nLeitura da lista B")
B = []
cont = 0
while cont < 10:
    X = int(input("Digite um valor: "))
    B.append(X)
    cont = cont + 1

R = []
for elemento in A:
    R.append(elemento)
for elemento in B:
    R.append(elemento)
# as 5 linhas acima podem ser substituídas por R = A + B

print("Lista A")
print(A)
print("Lista B")
print(B)
print("Lista R")
print(R)


print("\n\nFim do Programa")



