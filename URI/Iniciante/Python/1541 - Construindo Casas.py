import math

while True:
    valor = input()
    if valor == '0':
        break
    else:
        a,b,c = valor.split()
        metros = ((int(a)*int(b) *100) / int(c))
        print(int(math.sqrt(metros)))
