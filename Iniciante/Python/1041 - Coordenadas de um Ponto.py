A_1,B_1, = input().split(" ")

x = float(A_1)
y = float(B_1)

if x > 0 and y > 0:
    print ("Q1")
elif x < 0 and y > 0:
    print ("Q2")
elif x < 0 and y < 0:
    print ("Q3")
elif x > 0 and y < 0:
    print ("Q4")
elif x == 0 and y != 0:
    print ("Eixo Y")
elif x != 0 and y == 0:
    print ("Eixo X")
else:
    print ("Origem")
