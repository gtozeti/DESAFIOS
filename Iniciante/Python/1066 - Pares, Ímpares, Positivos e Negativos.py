numero = []
par = 0
impar = 0
pos = 0
neg = 0

for i in range(5):
  numero.append(int(input()))
 
for x in range(1,6):
    if ((numero[x-1] % 2) == 0 ) and (numero[x-1] > 0):
        par += 1
        pos += 1
    elif ((numero[x-1] % 2) == 0 ) and (numero[x-1] < 0):
        par += 1
        neg += 1
    elif ((numero[x-1] % 2) != 0 ) and (numero[x-1] < 0):
        impar += 1
        neg += 1
    elif ((numero[x-1] % 2) != 0 ) and (numero[x-1] > 0):
        impar += 1
        pos += 1
    else:
        par += 1

print("%i valor(es) par(es)"%par)
print("%i valor(es) impar(es)"%impar)
print("%i valor(es) positivo(s)"%pos)
print("%i valor(es) negativo(s)"%neg)
