n = int(input())
testes = []

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    ex = int(testes[y][0])
    primo = 0
    for k in range(1,ex+1):
        if ex % k == 0:
            primo += 1
    if primo == 2:
        print("%i eh primo"%ex)
    else:
        print("%i nao eh primo" % ex)
