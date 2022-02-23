A_1,B_1, = input().split(" ")

a = float(A_1)
b = float(B_1)

numeros = [a,b]
numeros_ordenados = sorted(numeros)

if (numeros_ordenados[1] % numeros_ordenados[0]) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
