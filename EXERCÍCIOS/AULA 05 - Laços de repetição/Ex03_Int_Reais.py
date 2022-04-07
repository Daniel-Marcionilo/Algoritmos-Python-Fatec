qtdeNum = int(input())

cont = 0
soma = 0

while cont < qtdeNum:
    numReal = float(input("Digite um valor real: "))
    soma = soma + numReal
    cont = cont + 1

print("Soma total dos números reais: {:.2f}".format(soma))
