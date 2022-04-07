#URI 1060 Ex02 Números Positivos - Aula 05

"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
"""


CONT = 1
POSITIVO = 0

while CONT <= 6 :
    X = float(input())
    if X != "":
            if X > 0:
                POSITIVO = POSITIVO + 1
                CONT = CONT + 1
            else:
                CONT = CONT + 1
print("{} valores positivos".format(POSITIVO))
        
    

