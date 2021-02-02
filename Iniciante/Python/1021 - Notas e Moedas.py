N = float(input())

notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

print ("NOTAS:")

for x in notas:
    print ("%i nota(s) de R$ %.2f"%((N/x),x))
    N %= (x)
    
print ("MOEDAS:")

for y in moedas:
    N = round(N,2)
    print ("%i moeda(s) de R$ %.2f"%((N/y),y))
    N %= (y)
