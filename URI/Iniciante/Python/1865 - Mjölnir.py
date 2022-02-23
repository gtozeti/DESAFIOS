n = int(input())
matriz = []

for x in range(n):
    matriz_ = input().split()
    matriz.append(matriz_)

for x in range(n):
    if matriz[x][0] == "Thor":
        print("Y")
    else:
        print("N")
