n1 = float(input())
a = 0
b = 0

while a == 0:
    if n1 >=0 and n1 <= 10:
        n2 = float(input())
        while b == 0:
            if n2 >=0 and n2 <= 10:
                media = (n1 + n2) / 2
                print("media = %.2f"%media)
                a = 1
                b = 1
            else:
                print("nota invalida")
                n2 = float(input())
    else:
        print("nota invalida")
        n1 = float(input())
