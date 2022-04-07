#URI 1066 Ex05 Pares, Ímpares, Positivos e Negativos - Aula 05

"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram
pares, quantos valores digitados foram ímpares, quantos valores digitados
foram positivos e quantos valores digitados foram negativos.
"""

CONT = 1
PARES = 0
IMPARES = 0
POSITIVOS = 0
NEGATIVOS = 0

while CONT <= 5:
    X = int(input())
    if X % 2 == 0:
        PARES = PARES + 1
    else:
        IMPARES = IMPARES + 1
    if X > 0:
        POSITIVOS = POSITIVOS + 1
    elif X < 0:
        NEGATIVOS = NEGATIVOS + 1
    CONT = CONT + 1
        
print("{} valor(es) par(es)".format(PARES))
print("{} valor(es) impar(es)".format(IMPARES))
print("{} valor(es) positivo(s)".format(POSITIVOS))
print("{} valor(es) negativo(s)".format(NEGATIVOS))
