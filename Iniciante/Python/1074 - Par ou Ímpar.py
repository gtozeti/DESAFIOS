N = int(input())
numero = []


for i in range(N):
  numero.append(int(input()))
 
for x in range(1,N+1):
    if ((numero[x-1] % 2) == 0 ) and (numero[x-1] > 0):
        print("EVEN POSITIVE")
    elif ((numero[x-1] % 2) == 0 ) and (numero[x-1] < 0):
        print("EVEN NEGATIVE")
    elif ((numero[x-1] % 2) != 0 ) and (numero[x-1] < 0):
        print("ODD NEGATIVE")
    elif ((numero[x-1] % 2) != 0 ) and (numero[x-1] > 0):
        print("ODD POSITIVE")
    else:
        print("NULL")
