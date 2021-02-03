numero = []
a = 0
b = 0

for i in range(6):
  numero.append(float(input()))
 
for x in range(1,7):
    if numero[x-1] > 0:
        b += 1
        a += numero[x-1]   
        
media = a / b
print("%i valores positivos"%(b))
print("%.1f"%(media))
