condicao = 0
matriz = []


while True:
    try:
        N = int(input())
        numero = N
        matriz = []
        pos1 = int(N/3)
        coringa = N - 1

        for i in range(numero):
            linha = []
            for j in range(numero):
                linha.append(0)
            matriz.append(linha)

        for x in range(numero):
            for y in range(numero):
                if x >= pos1 and x <= (N-1)-pos1 and y >= pos1 and y <= (N-1)-pos1:
                    matriz[x][y] = 1
                elif x == y and not (x >= pos1 and x <= (N-1)-pos1 and y >= pos1 and y <= (N-1)-pos1):
                    matriz[x][y] = 2
                elif y == coringa and not (x >= pos1 and x <= (N-1)-pos1 and y >= pos1 and y <= (N-1)-pos1):
                    matriz[x][y] = 3
                else:
                    matriz[x][y] = 0
            coringa -= 1

        meio = int((N - 1)/2)
        matriz[meio][meio] = 4

        for x in range(N):
            for y in range(N):
                print(matriz[x][y], end='')
            print()
        print()

    except EOFError:
        break
