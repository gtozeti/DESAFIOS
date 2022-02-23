while True:
    try:
        maior = 0
        n = int(input())
        testes = input().split()

        for x in range(n):
            if int(testes[x]) > maior:
                maior = int(testes[x])

        if maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
