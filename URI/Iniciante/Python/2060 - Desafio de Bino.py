n = int(input())
matriz = input().split()
mult = [2,3,4,5]
n2, n3, n4, n5 = 0, 0, 0 ,0

for x in range(n):
    for y in range(4):
        n1 = int(matriz[x])
        if n1 % mult[y] == 0:
            pos = y
            if pos == 0:
                n2 += 1
            elif pos == 1:
                n3 += 1
            elif pos == 2:
                n4 += 1
            else:
                n5 += 1

print("%d Multiplo(s) de 2"%n2)
print("%d Multiplo(s) de 3"%n3)
print("%d Multiplo(s) de 4"%n4)
print("%d Multiplo(s) de 5"%n5)
