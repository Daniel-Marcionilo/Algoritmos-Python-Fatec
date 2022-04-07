qtdeNum = int(input("Digite a quantidade de valores: "))

cont = 0
soma = 0

while cont < qtdeNum:
    numReal = float(input("Digite um valor real: "))
    if numReal > 0:
        soma = soma + numReal
        cont = cont + 1
    else:
        cont = cont + 1

print("Soma total dos números reais: {:.2f}".format(soma))
