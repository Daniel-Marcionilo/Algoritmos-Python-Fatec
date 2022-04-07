a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a < b + c and b < c + a and c < b + a:
    if a == b and b == c:
        triangulo = "EQUILÁTERO"
    elif a != b and b != c and c != a:
        triangulo = "ISÓSCELES"
    else:
        triangulo = "ESCALENO"

    print(f"Os valores formam um triângulo {triangulo}".upper())
   
else:
    print("Os valores informados, não podem formar um triângulo".upper())
