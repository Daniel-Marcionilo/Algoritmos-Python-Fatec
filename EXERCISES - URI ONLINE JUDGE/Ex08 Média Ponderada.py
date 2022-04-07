#URI 1079 Ex08 Média Ponderada - Aula 05

x = int(input())

cont = 0
media = []

while cont < x:
   notas = input().split()
   
   n1 = float(notas[0])
   n2 = float(notas[1])
   n3 = float(notas[2])

   media = (n1 * 2 + n2 * 3 + n3 * 5)/(10)

   print("{:.1f}".format(media))
   cont = cont + 1

