testes = int(input())
casos = []

for x in range(testes):
    casos_ = input().split()
    casos.append(casos_)

for x in range(testes):
    a = int(casos[x][0])
    b = int(casos[x][1])
    print(a+b)
