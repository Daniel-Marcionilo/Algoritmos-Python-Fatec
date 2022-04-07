n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 < n2:
	print("O menor dos dois números é: ", n1)
	print("E o maior número é: ", n2)
elif n2 < n1:
	print("O menor dos dois números é: ", n2)
	print("E o maior número é: ", n1)
else:
	print("Os números são iguais :)")
