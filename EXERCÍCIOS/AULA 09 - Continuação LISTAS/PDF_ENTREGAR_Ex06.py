"""
Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente
se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final,
apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é
necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter
os valores. 
"""

LMin = int(input("Digite o valor mínimo: "))
LMax = int(input("Digite o valor máximo: "))
if LMax < LMin:
    aux = LMax
    LMax = LMin
    LMin = aux
    
cont = 0
A = []

while cont < 10:
    x = (int(input("Digite um valor inteiro: ")))    
    if LMin <= x <= LMax:
        A.append(x)
    cont = cont + 1
    
cont = 0
for i in A:
   cont = cont + 1
   
print("\nLista A =", A)
print("\nQuantidade de elementos em A =", cont)
print("\nFim do programa")
