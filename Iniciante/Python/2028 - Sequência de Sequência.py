casos = 0
while True:

    try:
        n = int(input())
        su, valor, cont = 0, 0, 0
        matriz = []

        for x in range(1,n+1):
            su += x

        su += 1
        matriz.append(0)
        cont += 1

        while cont < su:
            for y in range(valor):
                matriz.append(valor)
                cont += 1
            valor += 1

        casos += 1

        if n >= 1:
            print("Caso %d: %d numeros" %(casos,su))
            print(*matriz)
            print()
        else:
            print("Caso %d: %d numero" % (casos, su))
            print(*matriz)
            print()

    except EOFError:
        break
