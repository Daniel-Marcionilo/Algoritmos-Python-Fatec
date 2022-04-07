"""
2. Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.

"""

minimo = int(input("Digite o valor mínimo: "))
maximo = int(input("Digite o valor máximo: "))

if maximo > minimo:
    cont = minimo
    
    while cont <= maximo:
        if cont % 5 == 0:
            print(cont)
        cont = cont + 1
else:
    print("ERRO! Valor mínimo maior que valor máximo")
