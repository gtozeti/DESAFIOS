soma = 0
a = 3
b = 2
for x in range(18):
    soma += a/b
    a += 2
    b *= 2
print("%.2f"%(soma+1))
