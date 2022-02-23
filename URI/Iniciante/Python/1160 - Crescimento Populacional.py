n = int(input())
testes = []

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    popA = int(testes[y][0])
    popB = int(testes[y][1])
    tA = int((float(testes[y][2])*popA)/100)
    tB = int((float(testes[y][3])*popB)/100)
    anos = 0
    while popA <= popB:
        popA += tA
        tA = int((float(testes[y][2]) * popA) / 100)
        popB += tB
        tB = int((float(testes[y][3]) * popB) / 100)
        anos += 1
        if anos > 100:
            print("Mais de 1 seculo.")
            break
    if anos <= 100:
        print("%i anos." % anos)
