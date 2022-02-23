a = 0
b = 0
soma = 0
while a == 0:
    n = int(input())
    if n == 0:
        a = 1
    else:
        c = n
        b = 0
        soma = 0
        while b < 5:
            if c % 2 == 0:
                soma += c
                b += 1
            c += 1
        print(soma)
