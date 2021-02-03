condicao = 0
matriz = []

while condicao == 0:

    N = int(input())
    numero = N
    expoente = 1
    tamanho = 0

    if numero == 0:
        condicao = 1
    else:
        matriz = []
        for i in range(numero):
            linha = []
            for j in range(numero):
                linha.append(1)
            matriz.append(linha)

        for x in range(numero):
            for y in range(numero):
                if y == 0:
                    matriz[x][y] = expoente
                else:
                    matriz[x][y] = matriz[x][y-1] * 2
            expoente *= 2

        tamanho = len(str(matriz[N-1][N-1]))

        for x in range(N):
            for y in range(N):
                if y == N - 1:
                    print(str(matriz[x][y]).rjust(tamanho), end='')
                else:
                    print(str(matriz[x][y]).rjust(tamanho), end=' ')
            print()
        print()
