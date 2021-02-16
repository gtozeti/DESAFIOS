while True:
    try:
        horas,minutos = input().split(":")

        total = (60 * int(horas)) + int(minutos)

        if total > (60*7):
            if int(horas) >= 9:
                sum = ((int(horas) - 8) * 60) + 60
                print("Atraso maximo:", sum)
            elif int(horas) >= 8 and int(horas) < 9:
                sum = 60 + int(minutos)
                print("Atraso maximo:", sum)
            else:
                sum = int(minutos)
                print("Atraso maximo:", sum)
        else:
            print("Atraso maximo: 0")

    except EOFError:
        break
