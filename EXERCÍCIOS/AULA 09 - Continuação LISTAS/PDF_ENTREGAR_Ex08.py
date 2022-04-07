"""
Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max]
sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de
valores rejeitados (lista R), bem como o tamanho de cada um.
"""

LMin = int(input("Digite o valor mínimo: "))
LMax = int(input("Digite o valor máximo: "))
N = int(input("Digite a quantidade de valores inteiros que serão informados: "))

if LMax < LMin:
    aux = LMax
    LMax = LMin
    LMin = aux
   
cont = 0
A = []
R = []
while cont < N:
    x = (int(input("Digite um valor inteiro: ")))    
    if x >= LMin and x <= LMax:
        A.append(x)
    else:
      R.append(x)  
    cont = cont + 1
print("\nLista A =", A)
print("\nQuantidade de elementos ACEITOS em A =", len(A))
print("\nLista R =", R)
print("\nQuantidade de elementos REJEITADOS em A =", len(R))
print("\nFim do programa")
