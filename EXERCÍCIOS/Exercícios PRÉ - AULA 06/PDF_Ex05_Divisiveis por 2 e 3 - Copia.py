"""
5. Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.
"""

#Ex05 Divisiveis por 2 e 3

x = 1

while x != 0:
    x = int(input())
    if x > 0:
        if x % 2 == 0 and x % 3 == 0:
            print(f"{x} Divisível por 2 e 3")
        else:
            print(f"{x} Não é divisível por 2 e 3")
