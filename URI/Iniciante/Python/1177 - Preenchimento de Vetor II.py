n = int(input())
vetor = [0]*1000
cont = 0

while cont <= 999:
    for y in range(n):
        vetor[cont] = y
        cont += 1
        if cont == 1000:
            break

for k in range(1000):
    print("N[%i] = %i"%(k,vetor[k]))
