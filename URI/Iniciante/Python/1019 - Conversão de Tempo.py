N = int(input())

seg = N
horas = int(seg / 3600)

seg %= 3600
minutos = int(seg / 60)

seg %= 60
segundos = int(seg / 1)

print ("%i:%i:%i"%(horas,minutos,segundos))
