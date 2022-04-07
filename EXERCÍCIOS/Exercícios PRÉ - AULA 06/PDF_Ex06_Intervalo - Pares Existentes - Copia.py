"""
6. Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito)
"""

N = 1
while N < 100:   
    N = int(input("Digite um número maior ou igual a 100: "))

soma_Pares = 0
cont = 1

while cont <= N:
        if cont % 2 == 0:
            soma_Pares = soma_Pares + cont
        cont = cont + 1

if soma_Pares > 0:
    print("Somatório dos valores pares =", soma_Pares)
    






