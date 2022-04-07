#URI 1064 Ex03 Números Positivos e Média - Aula 05

"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados,
com um dígito após o ponto decimal."""

CONT = 1
POSITIVO = 0
SOMA = 0
while CONT <= 6 :
    X = float(input())
    if X != "":
            if X > 0:
                SOMA = SOMA + X
                POSITIVO = POSITIVO + 1
                CONT = CONT + 1
            else:
                CONT = CONT + 1


#media igual a soma dos valores positivos dividido pela var positivo
MEDIA = SOMA/POSITIVO                
print("{} valores positivos".format(POSITIVO))
print("{:.1f}".format(MEDIA))    

