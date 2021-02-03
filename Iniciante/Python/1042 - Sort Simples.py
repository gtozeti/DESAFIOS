A_1,B_1,C_1 = input().split(" ")

a = int(A_1)
b = int(B_1)
c = int(C_1)

numeros = [a,b,c]
numeros_ordenados = sorted(numeros)

print("%i\n%i\n%i\n\n%i\n%i\n%i"%(numeros_ordenados[0],numeros_ordenados[1],numeros_ordenados[2],numeros[0],numeros[1],numeros[2]))
