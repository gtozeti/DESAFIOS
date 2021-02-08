n = int(input())
matriz = []

for x in range(n):
    matriz.append(int(input()))

for x in range(n):
    result = 2015 - matriz[x]
    if result > 0:
        print(result, "D.C.")
    elif result == 0:
        print("1 A.C.")
    else:
        print(abs(matriz[x] - 2015)+1, "A.C.")
