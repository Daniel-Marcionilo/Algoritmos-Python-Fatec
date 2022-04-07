"""
8. Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.

"""

x = int(input("Digite um número inteiro: "))

cont = 1

qtdeDivisor = 0

while cont <= x:

    if x % cont == 0: 
        qtdeDivisor = qtdeDivisor + 1
    
    cont = cont + 1

if qtdeDivisor == 2:
    print("{} é um número primo".format(x))
else:
    print("{} não é um número primo".format(x))

