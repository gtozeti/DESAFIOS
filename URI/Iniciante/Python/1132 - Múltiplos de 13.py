x = int(input())
y = int(input())

numeros = [x,y]
numeros_ord = sorted(numeros)

soma = 0

for k in range(numeros_ord[0],numeros_ord[1]+1):
    if k % 13 != 0:
        soma += k

print(soma)
