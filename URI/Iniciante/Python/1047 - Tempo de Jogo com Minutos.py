A_1,B_1,C_1,D_1 = input().split(" ")

a = int(A_1)
b = int(B_1)
c = int(C_1)
d = int(D_1)

hInicio = (a*60) + b
hFim = (c*60) + d

if hInicio > hFim:
    tempo = ((60*24)-hInicio) + hFim
    c = tempo
    horas = int(c / 60)
    c %= 60
    minutos = int(c)
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)"%(horas,minutos))
elif hInicio == hFim:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    tempo = hFim - hInicio
    c = tempo
    horas = int(c / 60)
    c %= 60
    minutos = int(c)
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)"%(horas,minutos))
