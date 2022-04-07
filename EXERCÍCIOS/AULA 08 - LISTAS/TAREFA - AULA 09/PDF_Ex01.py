#Tipos compostos em Python - Listas
"""
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento
por linha.
"""

lista = []
cont = 0
while cont < 10:
    x = int(input("Digite valor do {} elemento: ".format(cont)))
    lista.append(x)
    cont = cont + 1
    
for i in lista:
    print(i)

#Outra forma de fazer o laço
#
#cont = 0
#while cont < len(lista):
    #print(lista[cont])
    #cont = cont + 1
