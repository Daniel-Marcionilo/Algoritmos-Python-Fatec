"""
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em
um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma.
"""

L = []

NEG = []

POS = []

A = []

N = -1
while N <= 0 or N >= 50:
    N = int(input("Digite um número entre 0 e 50: "))

cont = 0

while cont < N:
    R = float(input("Digite um número real: "))
    A.append(R)
    cont = cont + 1

contN = 0
contP = 0
for i in A:
    if i >= 0:
        POS.append(i)
        contP = contP + 1
    else:
        NEG.append(i)
        contN = contN + 1


print("Lista A e seus respectivos valores\n")
print(A, "\n")
print("Lista de Positivos\n")
for p in POS:
    print("{:.2f}".format(p) + "\n")

print("Lista de Negativos\n")
for n in NEG:
    print("{:.2f}".format(n) + "\n")

print("Quantidade de valores POSITIVOS =", contP, "\n")
print("Quantidade de valores NEGATIVOS =", contN)

print("\n\nFim do programa")

