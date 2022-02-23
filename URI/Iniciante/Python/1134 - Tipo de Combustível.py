a = 0
codigo = 0
alcool = 0
gas = 0
diesel = 0

while a == 0:
    codigo = int(input())
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gas += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        a = 1

print("MUITO OBRIGADO")
print("Alcool:",alcool)
print("Gasolina:",gas)
print("Diesel:",diesel)
