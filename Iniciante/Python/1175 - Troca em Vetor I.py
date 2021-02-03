testes = [0]*20
testes2 = [0]*20
soma = 0

for x in range(20):
    testes[x] = int(input())

for y in reversed(range(20)):
    testes2[y] = testes[soma]
    soma += 1

for k in range(20):
    print("N[%i] = %i"%(k,testes2[k]))
