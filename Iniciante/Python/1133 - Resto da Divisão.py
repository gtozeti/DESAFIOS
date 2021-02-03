x = int(input())
y = int(input())

numeros = [x,y]
numeros_ord = sorted(numeros)

for k in range(numeros_ord[0]+1,numeros_ord[1]):
    if k % 5 == 2 or k % 5 == 3:
        print(k)
