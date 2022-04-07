"""
4. Reescreva um programa do exercício acima considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado.
"""

#Ex04, apenas positivos

x = int(input())

cont = 0

maior = 0

menor = 0

verificador = 0

while cont < x:
    num = float(input())
    if num > 0 :
        if verificador == 0 or num > maior:
            maior = num
               
        if verificador == 0 or num < menor:
            menor = num
        verificador = verificador + 1 #por que o verificador precisa ficar aqui?
    else:
        print("Digitou número negativo, mas vou seguir")
    #verificador = verificador + 1 não poderia colocar o verificador aqui?

    cont = cont + 1

if verificador > 0:
    print("Maior =", maior)
    print("Menor =", menor)
else:
    print("Nenhum valor válido")

