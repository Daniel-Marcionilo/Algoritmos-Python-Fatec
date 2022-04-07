N = int(input("Digite o N° de termos que deseja: "))
P = int(input("Digite o primeiro Termo: "))
R = int(input("Digite o valor da razão: "))

if N > 0 :
    SOMA = 0
    CONT = 1
    N2 = N
    N = 0
    while CONT <= N2:
        PG = P * (R ** (N))
        SOMA = SOMA + PG
        N = N + 1
        CONT = CONT + 1
        print(PG)
        
print(f"Soma total dos termos: {SOMA}")

Ex 02 - TOTAL DE POSITIVOS E NEGATIVOS

TOTAL_POSITIVO = 0
TOTAL_NEGATIVO = 0
X = 1
while X != 0:
    X = int(input("Digite um número: "))
    if  X > 0:
        TOTAL_POSITIVO = TOTAL_POSITIVO + X
    else:
        TOTAL_NEGATIVO = TOTAL_NEGATIVO + X

print(f"Total dos positivos = {TOTAL_POSITIVO}")
print(f"Total dos negativos = {TOTAL_NEGATIVO}")
