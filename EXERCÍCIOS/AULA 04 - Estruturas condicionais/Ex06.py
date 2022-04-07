nome = input("Digite o nome do Lutador: ")
peso = float(input("Digite o peso do Lutador: "))

if peso < 65:
	categoria = "Pena"
	
elif peso >= 65 and peso < 72:
	categoria = "Leve"
	
elif peso >= 72 and peso < 79:
	categoria = "Ligeiro"
	
elif peso >= 79 and peso < 86:
	categoria = "Meio Médio"
	
elif peso >= 86 and peso < 93:
	categoria = "Médio"
	
elif peso >= 93 and peso < 100:
	categoria = "Meio Pesado"
	
elif peso >= 100:
	categoria = "Pesado"

print("Nome: ", nome)
print("Peso: ", peso)
print("O lutador {} pesa {:.1f} kg e se enquadra na categoria {}".format(nome, peso, categoria))
