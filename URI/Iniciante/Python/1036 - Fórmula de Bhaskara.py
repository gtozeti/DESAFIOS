A1,B1,C1 = input().split(" ")

A = float(A1)
B = float(B1)
C = float(C1)

delta = (B**2) - (4*A*C)

if delta > 0 and A > 0:
    x1 = (-B + (delta ** 0.5)) / (2*A)
    x2 = (-B - (delta ** 0.5)) / (2*A)
    print ("R1 = %.5f\nR2 = %.5f"%(x1,x2))

else:
    print("Impossivel calcular")
