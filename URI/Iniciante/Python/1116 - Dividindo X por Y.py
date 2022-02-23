n = int(input())
testes = []
resultado = 0

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    a = int(testes[y][0])
    b = int(testes[y][1])

    if b == 0:
        print("divisao impossivel")
    else:
        resultado = a/b
        print("%.1f"%resultado)
