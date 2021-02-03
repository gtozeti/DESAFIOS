n = int(input())
testes = []

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    a = int(testes[y][0])
    c = 0
    soma = 0
    while c < int(testes[y][1]):
        if a % 2 != 0:
            soma += a
            c += 1
        a += 1
    print(soma)
