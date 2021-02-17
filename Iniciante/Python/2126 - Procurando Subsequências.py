caso = 1
while True:
    try:
        n1 = str(input())
        n2 = str(input())

        total = n2.count(n1)

        if total > 0:
            print("Caso #{}:\nQtd.Subsequencias: {}\nPos: {}\n".format(caso,total,n2.rfind(n1)+1))

        else:
            print("Caso #{}:\nNao existe subsequencia\n".format(caso))

        caso += 1

    except EOFError:
        break
