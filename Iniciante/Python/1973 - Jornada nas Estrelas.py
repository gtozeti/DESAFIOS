def main():
    from sys import stdin


    n = int(stdin.readline())
    matriz = list(map(int, stdin.readline().split()))

    star, ovelha, vezes = 0, 0, 0
    total = sum(matriz)

    while 0 <= star < n:

        cond = int(matriz[star])

        if cond % 2 == 0 and cond != 0:
            matriz[star] = cond - 1
            star -= 1
            ovelha += 1
            if vezes == (star+1):
                vezes += 1
        elif cond % 2 != 0 and cond != 0:
            matriz[star] = cond - 1
            star += 1
            ovelha += 1
            if vezes < star:
                vezes += 1
        else:
            break

    print(vezes, (total - ovelha))
if __name__ == "__main__":
    main()
