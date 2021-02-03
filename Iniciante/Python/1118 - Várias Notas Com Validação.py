n1 = float(input())
a = 0
b = 0
c = 0
d = 0
while c == 0:
    a = 0
    b = 0
    d = 0
    while a == 0:
        if n1 >=0 and n1 <= 10:
            n2 = float(input())
            while b == 0:
                if n2 >=0 and n2 <= 10:
                    media = (n1 + n2) / 2
                    print("media = %.2f"%media)
                    print("novo calculo (1-sim 2-nao)")
                    validacao = int(input())
                    while d == 0:
                        if validacao == 1:
                            d = 1
                            a = 1
                            b = 1
                            n1 = float(input())
                        elif validacao == 2:
                            d = 1
                            b = 1
                            a = 1
                            c = 1
                        else:
                            print("novo calculo (1-sim 2-nao)")
                            validacao = int(input())
                else:
                    print("nota invalida")
                    n2 = float(input())
        else:
            print("nota invalida")
            n1 = float(input())
