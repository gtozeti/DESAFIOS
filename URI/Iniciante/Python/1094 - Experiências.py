n = int(input())
testes = []
cobaias = 0
rato = 0
sapo = 0	
coelho = 0

for x in range(n):
    testes_ = input().split()
    testes.append(testes_)

for y in range(n):
    cobaias += int(testes[y][0])
    if testes[y][1] == "R":
        rato += int(testes[y][0])
    elif testes[y][1] == "S":
        sapo += int(testes[y][0])
    else:
        coelho += int(testes[y][0])

print("Total: %i cobaias"%cobaias)
print("Total de coelhos:",coelho)
print("Total de ratos:",rato)
print("Total de sapos:",sapo)
print("Percentual de coelhos: %.2f %%"%((coelho*100)/cobaias))
print("Percentual de ratos: %.2f %%"%((rato*100)/cobaias))
print("Percentual de sapos: %.2f %%"%((sapo*100)/cobaias))
