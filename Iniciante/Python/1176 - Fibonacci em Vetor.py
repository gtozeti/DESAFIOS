testes = [0]*61
casos = []
a = 0
b = 1
cont = 0
for x in range(61):
    testes[x] = a
    c = a + b
    a = b
    b = c
    cont += 1

n = int(input())
for k in range(n):
    l = input().split()
    casos.append(l)

for j in range(n):
    f = int(casos[j][0])
    print("Fib(%i) = %i"%(f,testes[f]))
