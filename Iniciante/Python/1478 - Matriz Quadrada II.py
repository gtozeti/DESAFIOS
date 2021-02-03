condicao = 0
matriz = []

while condicao == 0:

    N = int(input())
    numero = N
    elemento = 1

    if numero == 0:
        condicao = 1
    else:
        matriz = []
        for i in range(numero):
            linha = []
            for j in range(numero):
                linha.append(elemento)
            matriz.append(linha)

        for x in range(numero):
            for y in range(numero):
                if x == y:
                    matriz[x][y] = 1
                else:
                    matriz[x][y] = matriz[x][y-1] + 1

        for x in reversed(range(numero)):
            for y in reversed(range(numero)):
                if y < x:
                    matriz[x][y] = 1
                    matriz[x][y] = matriz[x][y + 1] + 1

        for x in range(N):
            for y in range(N):
                if y == N - 1:
                    print(f'{matriz[x][y]:>3}', end='')
                else:
                    print(f'{matriz[x][y]:>3}', end=' ')
            print()
        print()
