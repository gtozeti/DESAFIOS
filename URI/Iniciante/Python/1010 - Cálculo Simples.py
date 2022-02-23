a_1,b_1,c_1 = input().split(" ")
a_2,b_2,c_2 = input().split(" ")

a1 = int(a_1)
b1 = int(b_1)
c1 = float(c_1)
a2 = int(a_2)
b2 = int(b_2)
c2 = float(c_2)

soma = (b1*c1)+(b2*c2)

print("VALOR A PAGAR: R$","%.2f" % soma)
