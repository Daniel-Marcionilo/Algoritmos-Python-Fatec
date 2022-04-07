"""
9. Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1. 
"""

# A sequência de Fibonacci funciona assim:
# 0    -   1 - inicio
# 1° T  2° T
# 3° T = 1° T + 2° T
# e assim sucessivamente para N termos solicitados

x = int(input())

if x == 1:
    print("0")
else:
    

    t1 = 0

    t2 = 1

    cont = 3

    print(t1, end = " ")
    print(t2, end = " ")

    while cont <= x:
        r = t1 + t2
        print("{}".format(r), end = " ")
        t1 = t2
        t2 = r
        cont += 1



