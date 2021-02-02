A1,B1,C1,D1 = input().split(" ")

A = int(A1)
B = int(B1)
C = int(C1)
D = int(D1)

if B > C and D > A and (C+D) > (A+B) and C > 0 and D > 0 and ((A % 2) == 0):
    print("Valores aceitos")
else:
        print("Valores nao aceitos")
