n = int(input())
testes = []
perfeito = 0

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    ex = int(testes[y][0])
    perfeito = 0
    for k in range(1,ex):
        if ex % k == 0:
            perfeito += k
    if perfeito == ex:
        print("%i eh perfeito"%ex)
    else:
        print("%i nao eh perfeito" % ex)
