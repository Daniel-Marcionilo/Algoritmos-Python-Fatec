"""
Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número
fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa
anterior.
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

while cont < N:
    x = (int(input("Digite um valor inteiro: ")))    
    if x >= LMin and x <= LMax:
        A.append(x)

    cont = cont + 1
print("\nLista A =", A)
print("\nQuantidade de elementos em A =", len(A))
print("\nFim do programa")
