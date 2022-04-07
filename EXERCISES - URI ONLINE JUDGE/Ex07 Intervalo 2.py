#URI 1072 Ex07 Intervalo 02 - Aula 05

x = int(input())

cont = 1
dentro = 0
fora = 0

while cont <= x:
   num = int(input())
   if num >= 10 and num <= 20:
      dentro = dentro + 1
   else:
      fora = fora + 1
   cont = cont + 1
   
print("{} in".format(dentro))
print("{} out".format(fora))

      

    
