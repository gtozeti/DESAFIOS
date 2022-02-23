numero = []
a = 0
b = 0

for i in range(100):
    numero.append(int(input()))

for x in range(100):
    if numero[x] > a:
        a = numero[x]
        b = x+1

print(a)
print(b)
