"""
1. Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
"""

x = int(input("Digite um número: "))

cont = 1
tabuada = 1
r = 0
while cont <= 10:
    r = x * tabuada
    print("{} x {} = {}".format(x, tabuada, r))
    tabuada = tabuada + 1
    
    cont = cont + 1

