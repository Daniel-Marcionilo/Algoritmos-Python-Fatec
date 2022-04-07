#URI 1065 Ex04 Pares entre Cinco Núermos - Aula 05

"""Faça um programa que leia 5 valores inteiros. Conte quantos destes
valores digitados são pares e mostre esta informação."""

CONT = 1
PARES = 0

while CONT <= 5:
    X = int(input())
    if X % 2 == 0:
        PARES = PARES + 1
        CONT = CONT + 1
    else:
        CONT = CONT + 1
print("{} valores pares".format(PARES))

