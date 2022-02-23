A_1,B_1,C_1,D_1 = input().split()

a = int(A_1)
b = int(B_1)
c = int(C_1)
d = int(D_1)

ABC = abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b)
ABD = abs(b-d) < a < (b+d) and abs(a-d) < b < (a+d) and abs(a-b) < d < (a+b)
ADC = abs(d-c) < a < (d+c) and abs(a-c) < d < (a+c) and abs(a-d) < c < (a+d)
DBC = abs(b-c) < d < (b+c) and abs(d-c) < b < (d+c) and abs(d-b) < c < (d+b)

if ABC == True or ABD == True or ADC == True or DBC == True:
    print("S")
else:
    print("N")
