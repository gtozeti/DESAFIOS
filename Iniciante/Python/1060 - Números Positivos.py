numero = []
for i in range(6):
  numero.append(float(input()))
a  = 0

for x in range(1,7):
    if numero[x-1] > 0:
        a += 1
print("%i valores positivos"%(a))
