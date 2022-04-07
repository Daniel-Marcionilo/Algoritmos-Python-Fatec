l1 = []
l2 = []

x = 0
while x < 10:
    element = l1.append(int(input("Digite um número: ")))
    x = x + 1
    
x = 0
while x < 10:
    element = l2.append(int(input("Digite um número: ")))
    x = x + 1

print(l1, "\n")
print(l2, "\n")

juntar = l1 + l2
print(juntar)

