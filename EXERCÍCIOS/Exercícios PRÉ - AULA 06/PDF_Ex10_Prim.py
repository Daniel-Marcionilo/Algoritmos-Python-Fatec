"""
10. Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.
"""

# A sequência de Fibonacci funciona assim:
# 0    -   1 - inicio
# 1° T  2° T
# 3° T = 1° T + 2° T
# e assim sucessivamente para N termos solicitados

x = int(input("Digite um número de termos: "))

prim = int(input("Digite outro número: "))

t1 = 0

t2 = 1

cont = 0

#print(t1, end = " ")
#print(t2, end = " ")

while cont < x:
    r = t1 + t2
    if t1 > prim:
        print("{}".format(t1), end = " ")
        cont += 1
    t1 = t2
    t2 = r
    


