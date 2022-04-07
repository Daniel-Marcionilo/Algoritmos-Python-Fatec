#URI 1080 Ex09 Maior e Posição - Aula 05

x = 0
cont = 0
n = 0
posicao = [n] * 10
aux = 0
maior = 0

while cont < 10:
   x = int(input())
   if x > aux:
      maior = x
      aux = x
   posicao[n] = x
   n = n + 1
   cont = cont + 1

print(maior)
print(posicao.index(maior)+1) 
