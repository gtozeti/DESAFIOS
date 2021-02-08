A_1,B_1 = input().split()

a = int(A_1)
b = int(B_1)

if a == b:
    print(a)
else:
    ordem = [a,b]
    ordem = sorted(ordem)
    print(ordem[1])
