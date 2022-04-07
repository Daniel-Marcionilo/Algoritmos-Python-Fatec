"""
7. Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos.
"""

x = 0
while x <= 0:
    x = int(input("Digite um número maior que zero: "))
    
maior = 0

menor = 0

soma = 0

qtde = 0

media = 0

validador = 0

while x != 0 and x > 0:
    qtde = qtde + 1
    
    soma = soma + x
    
    if validador == 0 or x > maior:
        maior = x
    if validador == 0 or x < menor:
        menor = x

    validador = validador + 1
    x = int(input())
    
    while x == 0:
        x = int(input("INVÁLIDO! Digite um número maior que zero: "))
    
  
if validador > 0:
    media = soma / qtde

    print("Maior =", maior)
    print("Menor =", menor)
    print("Quantidade =", qtde)
    print("Soma =", soma)
    print("Media =", media)
#else:
    #print("Números digitados inválidos")

