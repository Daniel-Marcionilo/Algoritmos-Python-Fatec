N = int(input("Digite o valor de N: "))
P = int(input("Digite o valor de P: "))
R = int(input("Digite o valor de R: "))

SOMA = 0

while N > 0:

    PG = (P*(R**(N-1)))
    SOMA = SOMA + PG  
    N = N - 1
    print(PG)

print(f"Soma total dos termos: {SOMA}")
