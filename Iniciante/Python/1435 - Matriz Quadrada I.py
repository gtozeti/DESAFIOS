condicao = 0
matriz = []

while condicao == 0:
    N = int(input())
    numero = N
    elemento = 1
    cond1 = 0
    cond2 = 0
    if numero == 0:
        condicao = 1
    else:
        matriz = []
        for i in range(numero):
            linha = []
            for j in range(numero):
                linha.append(elemento)
            matriz.append(linha)

        numero -= 2
        cond2 = numero

        while numero > 0:
            elemento += 1
            cond1 += 1
            for x in range(cond1,cond2+1):
                for y in range(cond1,cond2+1):
                    matriz[x][y] = elemento
            cond2 -= 1
            numero -= 2

        for x in range(N):
            for y in range(N):
                if y == N - 1:
                    print(f'{matriz[x][y]:>3}', end='')
                else:
                    print(f'{matriz[x][y]:>3}', end=' ')
            print()
        print()
