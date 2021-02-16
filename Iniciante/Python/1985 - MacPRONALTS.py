n = int(input())
matriz = []
item = ["1001","1002","1003","1004","1005"]
valor = [1.50, 2.50, 3.50, 4.50, 5.50]
soma = 0

for x in range(n):
    matriz_ = input().split()
    matriz.append(matriz_)

for x in range(n):
    pos = 0
    for y in item:
        if y == matriz[x][0]:
            soma += (float(matriz[x][1]) * valor[pos])
        pos += 1

print("%.2f"%soma)
