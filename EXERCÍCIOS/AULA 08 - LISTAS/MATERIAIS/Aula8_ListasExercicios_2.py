# Tipos compostos em Python - Listas
# feito na Aula 8 em 27/09
#
# Exercício 2 das Tarefas da Aula 9
#
# O enunciado que consta do PDF ficou incompleto. Então aqui está o
# enunciado completo
#
# Escreva um programa que leia do teclado uma lista com tamanho de 10
# elementos obrigatoriamente positivos. Valores negativos e o zero
# devem ser deconsiderados. Ao final a lista deve conter os 10 elementos
# válidos. Exiba a lista na ordem inversa à ordem de leitura,
# sendo um elemento por linha da tela.


L = []
cont = 0
while cont < 10:
    X = int(input("Digite o elemento {} da lista: ".format(cont)))
    if X > 0:
        L.append(X)
        cont = cont + 1

print("\nElementos da lista na ordem inversa")
cont = 9
while cont >= 0:
    print(L[cont])
    cont = cont - 1

print("\n\nFim do Programa")



