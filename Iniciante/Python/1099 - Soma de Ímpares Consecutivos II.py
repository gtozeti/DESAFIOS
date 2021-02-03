n = int(input())
testes = []
impar = 0
a = 0
b = 0

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    a = int(testes[y][0])
    b = int(testes[y][1])
    if (a < b) and (abs(a-b) != 1):
        for z in range(a+1, b):
            if z %2 != 0:
                impar += z
        print(impar)
        impar = 0

    elif (a > b) and (abs(a-b) != 1):
        for z in range(b+1, a):
            if z %2 != 0:
                impar += z
        print(impar)
        impar = 0
    else:
        print(0)
