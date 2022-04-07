x = 0

lista = []
while x < 10:
    element = lista.append(int(input("Digite um número: ")))
    x = x + 1
    
lAux = lista[:]
aumenta = 0
diminui = x - 1
cont = 0
while cont < x:
    lista[aumenta] = lAux[diminui]
    diminui = diminui - 1
    aumenta = aumenta + 1
    cont = cont + 1
    
#lista[0] = lAux [5]
#lista[1] = lAux [4]
#lista[2] = lAux [3]
#lista[3] = lAux [2]
#lista[4] = lAux [1]
#lista[5] = lAux [0]

print(lista)

    
