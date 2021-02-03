A_1,B_1 = input().split(" ")

a = int(A_1)
b = int(B_1)

if a > b:
    horas = (24-a) + b
    print("O JOGO DUROU %i HORA(S)"%(horas))
elif a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    horas = b - a
    print("O JOGO DUROU %i HORA(S)"%(horas))
