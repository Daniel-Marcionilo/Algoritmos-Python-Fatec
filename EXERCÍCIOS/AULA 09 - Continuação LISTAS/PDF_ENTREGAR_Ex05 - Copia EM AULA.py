"""
Escreva um programa que leia um número N (obrigatoriamente entre 1 e 50 – o programa deve garantir isso em
um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma.
"""

N = int(input("Digite N (entre 1 e 50): ")) 
while N < 1 or N > 50:
    print("Valor inválido")
    N = int(input("Digite um número entre 1 e 50: "))

A = []
cont = 0
while cont < N:
    x = float(input("Digite um valor real: "))
    A.append(x)
    cont = cont + 1

Neg = []
ContNeg = 0
Pos = []
ContPos = 0
##i = 0
##while i < N:
##    if A[i] < 0:
##        Neg.append(A[i])
##        contNeg = ContNeg + 1
##    else:
##        Pos.append(A[i])
##        contPos = ContPos + 1
##    i = i + 1

for X in A:
    if X < 0:
        Neg.append(X)
        contNeg = ContNeg + 1
    else:
        Pos.append(X)
        contPos = ContPos + 1
    
print("\nLista A contém {} elementos: ".format(N))
print(A)

print("\nLista Neg contém {} elementos: ".format(ContNeg))
print(Neg)

print("\nLista Pos contém {} elementos: ".format(ContPos))
print(Pos)

print("\n\nFim do programa")

