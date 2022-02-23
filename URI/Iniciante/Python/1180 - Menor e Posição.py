n = int(input())
teste = input().split()
cond = 0
num = int(teste[n-1])
pos = 0

for x in range(n):
    cond = int(teste[x])
    if cond < num:
        pos = x
        num = cond

print("Menor valor: %i"%(int(teste[pos])))
print("Posicao:",pos)
