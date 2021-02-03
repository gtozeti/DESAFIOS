x = int(input())
y = int(input())

numeros = [x,y]
numeros_ = sorted(numeros)

soma = 0

for a in range(numeros_[0]+1,numeros_[1]):
    if a %2 != 0:
        soma += a

print(soma)
