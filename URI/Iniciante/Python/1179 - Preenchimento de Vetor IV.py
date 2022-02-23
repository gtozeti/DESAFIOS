par = [0]*5
impar = [0]*5
p = 0
i = 0

testes = []

condicao = 0

for x in range(15):
    testes_ = input().split()
    testes.append(testes_)

for y in range(15):
    condicao = int(testes[y][0])
    if condicao % 2 == 0:
        par[p] = condicao
        p += 1
        if p == 5:
            p = 0
            for k in range(5):
                print("par[%i] = %i"%(k,par[k]))
    else:
        impar[i] = condicao
        i += 1
        if i == 5:
            i =0
            for k in range(5):
                print("impar[%i] = %i"%(k,impar[k]))

for k in range(i):
    print("impar[%i] = %i"%(k,impar[k]))

for k in range(p):
    print("par[%i] = %i"%(k,par[k]))
