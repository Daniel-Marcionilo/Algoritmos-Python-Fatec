#URI 1094 Ex10 Experiências  - Aula 05

"""
Organizar os experimentos de um lab.
Calcular a qtde de cobaias que foram utilizadas no lab + o percentual
decada tipo de cobaia utilizada

3 tipos de Cobaias

S - Sapos
R - Ratos
C - Coelhos
"""

x = int(input())

cont = 0
qtdeC = 0
qtdeR = 0
qtdeS = 0
totalC = 0

while cont < x:
   cobaias = input().split()
   cobaias[1] = cobaias[1].upper()
   cobaias[0] = int(cobaias[0])
   totalC = totalC + cobaias[0]
   if cobaias[1] == "C":
      qtdeC = qtdeC + cobaias[0]
   elif cobaias[1] == "R":
      qtdeR = qtdeR + cobaias[0]
   elif cobaias[1] == "S":
      qtdeS = qtdeS + cobaias[0]
   cont = cont + 1

pC = (qtdeC / totalC) * 100
pR = (qtdeR / totalC) * 100
pS = (qtdeS / totalC) * 100

print("Total: {} cobaias".format(totalC))
print("Total de coelhos: {}".format(qtdeC))
print("Total de ratos: {}".format(qtdeR))
print("Total de sapos: {}".format(qtdeS))
print("Percentual de coelhos: {:.2f} %".format(pC))
print("Percentual de ratos: {:.2f} %".format(pR))
print("Percentual de sapos: {:.2f} %".format(pS))


    
