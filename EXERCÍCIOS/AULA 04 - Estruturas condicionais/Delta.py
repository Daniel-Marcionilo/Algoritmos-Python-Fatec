a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b * b) - (4 * a * c)

raizdelta = delta ** (1/2)

if delta > 0:
	x1 = (-b + raizdelta) / (2 * a)
	x2 = (-b - raizdelta) / (2 * a)
	print("x1 = {:.2f} x2 = {:.2f}".format(x1, x2))

elif delta == 0:
    	x1 = -b / (2 * a)
    	print("x = {}".format(x1))
else:
	print("Não há raízes reais")
