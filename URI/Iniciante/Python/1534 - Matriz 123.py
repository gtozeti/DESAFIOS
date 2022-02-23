condicao = 0
matriz = []


while True:
    try:
        N = int(input())
        numero = N
        coringa = N - 1
        matriz = []

        for i in range(numero):
            linha = []
            for j in range(numero):
                linha.append(0)
            matriz.append(linha)

        for x in range(numero):
            for y in range(numero):
                if x == y:
                    if numero % 2 == 0:
                        matriz[x][y] = 1
                    else:
                        meio = int((numero-1)/2)
                        matriz[x][y] = 1
                        matriz[meio][meio] = 2
                elif y == coringa:
                    matriz[x][coringa] = 2
                else:
                    matriz[x][y] = 3
            coringa -= 1

        for x in range(N):
            for y in range(N):
                print(matriz[x][y], end='')
            print()

    except EOFError:
        break
