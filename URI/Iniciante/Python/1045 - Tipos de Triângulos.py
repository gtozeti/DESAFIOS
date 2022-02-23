
A_1,B_1,C_1 = input().split(" ")

a1 = float(A_1)
b1 = float(B_1)
c1 = float(C_1)

numeros = [a1,b1,c1]
numeros_ordenados = sorted(numeros,reverse=True)

a = numeros_ordenados[0]
b = numeros_ordenados[1]
c = numeros_ordenados[2]

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif (a**2 == (b**2 + c**2)) and (a == b and a == c):
    print("TRIANGULO RETANGULO")
    print("TRIANGULO EQUILATERO")
elif (a**2 == (b**2 + c**2)) and (a == b or a == c or c == b):
    print("TRIANGULO RETANGULO")
    print("TRIANGULO ISOSCELES")
elif (a**2 == (b**2 + c**2)):
    print("TRIANGULO RETANGULO")
elif (a**2 > (b**2 + c**2)) and (a == b and a == c):
    print("TRIANGULO OBTUSANGULO")
    print("TRIANGULO EQUILATERO")
elif (a**2 > (b**2 + c**2)) and (a == b or a == c or c == b):
    print("TRIANGULO OBTUSANGULO")
    print("TRIANGULO ISOSCELES")
elif (a**2 > (b**2 + c**2)):
    print("TRIANGULO OBTUSANGULO")
elif (a**2 < (b**2 + c**2)) and (a == b and a == c):
    print("TRIANGULO ACUTANGULO")
    print("TRIANGULO EQUILATERO")
elif (a**2 < (b**2 + c**2)) and (a == b or a == c or c == b):
    print("TRIANGULO ACUTANGULO")
    print("TRIANGULO ISOSCELES")
elif (a**2 < (b**2 + c**2)):
    print("TRIANGULO ACUTANGULO")
