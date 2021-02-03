a = []
b = 1
while b == 1:
    n = int(input())
    a = []
    if n == 0:
        b = 0
    else:
        for x in range(1,n+1):
            a.append(x)
        print(*a)
