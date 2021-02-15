n = int(input())
matriz = []
nota, pos = 0, 0

for x in range(n):
    matriz_ = input().split()
    matriz.append(matriz_)

for x in range(n):
    if float(matriz[x][1]) > nota:
        nota = float(matriz[x][1])
        pos = x
if nota < 8:
    print("Minimum note not reached")
else:
    print(matriz[pos][0])
