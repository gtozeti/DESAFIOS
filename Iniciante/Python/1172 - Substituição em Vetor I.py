testes = [0]*10

for x in range(10):
    testes[x] = int(input())
for y in range(10):
    if testes[y] <= 0:
        testes[y] = 1
    print("X[%i] = %i" %(y, testes[y]))
