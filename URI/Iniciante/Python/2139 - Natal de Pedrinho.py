from datetime import date
while True:
    try:
        mes_, dia_ = input().split()

        dia = date(2016,int(mes_),int(dia_))
        natal = date(2016,12,25)

        dif = (natal - dia).days

        if dif == 0:
            print("E natal!")
        elif dif == 1:
            print("E vespera de natal!")
        elif dif < 0:
            print("Ja passou!")
        else:
            print("Faltam {} dias para o natal!".format(dif))

    except EOFError:
        break
