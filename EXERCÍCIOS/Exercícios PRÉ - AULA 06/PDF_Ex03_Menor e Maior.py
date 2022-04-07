"""
3. Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela.
"""

x = int(input())

cont = 0

menor = 0

maior = 0

while cont < x:
    num = float(input())
    
    if cont == 0:
        menor = num
        maior = num

    if num > maior:
        maior = num
    else:
        maior = maior

    if num < menor:
        menor = num
    else:
        menor = menor
    cont = cont + 1

print("Maior =", maior)
print("Menor =", menor)

    


