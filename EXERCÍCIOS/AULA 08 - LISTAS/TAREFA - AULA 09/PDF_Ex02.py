lista = []
cont = 0
while cont < 10:
    x = int(input("Digite um valor positivo: "))
    if x > 0:
        lista.insert(0,x)
        cont = cont + 1
print(lista)
