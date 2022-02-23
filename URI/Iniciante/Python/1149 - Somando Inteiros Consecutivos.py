a = input().split()
A = int(a[0])
N = 0
soma = 0

for x in range(1,len(a)):
    if int(a[x]) > 0:
        for k in range(1,int(a[x])):
            soma += A + k

print(soma+A)
