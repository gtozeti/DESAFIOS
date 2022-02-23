x = int(input())
b = 0
z = 0
soma = 0
qtd = 0

while b == 0:
    z = int(input())
    if z > x:
        b = 1

for k in range(x, z):
    if soma > z:
        break
    else:
        soma += k
        qtd += 1

print(qtd)
