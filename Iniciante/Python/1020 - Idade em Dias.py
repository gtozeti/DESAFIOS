N = int(input())

d = N
anos = int(d / 365)

d %= 365
meses = int(d / 30)

d %= 30
dias = int(d / 1)

print ("%i ano(s)\n%i mes(es)\n%i dia(s)"%(anos,meses,dias))
