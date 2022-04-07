# Tipos compostos em Python - Listas
"""

Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos, obrigatoriamente positivos.
Valores negativos e zero devem ser desconsiderados. Ao final da lista deve conter os 10 elementos válidos.
Exiba a lista na ordem inversa à ordem de leitura, sendo um elemento por linha da tela.

"""

lista = []
cont = 0
while cont < 10:
    x = int(input("Digite um valor positivo: "))
    if x > 0:
        lista.append(x)
        cont = cont + 1
        
cont = 9
while cont >= 0:
    print(lista[cont])
    cont = cont - 1
