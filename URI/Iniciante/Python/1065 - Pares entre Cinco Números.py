numero = []
b = 0
for i in range(5):
  numero.append(int(input()))
 
for x in range(1,6):
    if (numero[x-1] % 2) == 0:
        b += 1
        
print("%i valores pares"%(b))
