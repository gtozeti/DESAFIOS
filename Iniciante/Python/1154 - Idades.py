x = 0
contador = 0
soma = 0
while x == 0:
    a = int(input())
    if a > 0:
        soma += a
        contador += 1
    else:
        x = 1

print("%.2f"%(soma/contador))
