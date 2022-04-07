from random import randint

N = -1
while N <= 0 or N >= 50:
    N = int(input("Digite um número entre 0 e 50: "))

if N > 0 and N < 50:
    cont = 0
    L = []
    while cont < N:
        x = randint(0, 1000)
        L.append(x)
        cont = cont + 1
        
for elemento in L:
    print(elemento)
