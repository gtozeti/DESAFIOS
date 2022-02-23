n = int(input())
a = 0
b = 1
d = []
cont = 0

while cont < n:
    d.append(a)
    c = a + b
    a = b
    b = c
    cont += 1

print(*d)
