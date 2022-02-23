testes = [0]*10
testes[0] = int(input())
for x in range(1,10):
    testes[x] = testes[x-1]*2

for x in range(10):
    print("N[%i] = %i"%(x,testes[x]))
