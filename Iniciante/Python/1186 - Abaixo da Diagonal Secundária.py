operacao = input()
matriz = []
soma = 0
media = 0
total = 0
linhas = 12

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "S":
    for x in range(12):
        linhas -= 1
        for y in range(12):
           if y > linhas:
               soma += float(matriz[x][y])
    print("%.1f"%soma)
else:
    for x in range(12):
        linhas -= 1
        for y in range(12):
            if y > linhas:
                media += float(matriz[x][y])
                total += 1
    media = media/total
    print("%.1f"%media)
