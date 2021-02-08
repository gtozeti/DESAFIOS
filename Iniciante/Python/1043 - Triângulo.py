A_1,B_1,C_1 = input().split(" ")

a = float(A_1)
b = float(B_1)
c = float(C_1)

c1 = (abs(b-c)<a<(b+c))
c2 = (abs(a-c)<b<(a+c))
c3 = (abs(a-b)<c<(a+b))

if c1 == True and c2 == True and c3 == True:
    perimetro = a+b+c
    print("Perimetro = %.1f"%perimetro)
else:
    area = ((a+b)*c/2)
    print("Area = %.1f"%area)
