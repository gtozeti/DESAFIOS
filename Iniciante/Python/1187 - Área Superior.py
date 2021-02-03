operacao = input()
matriz = []
soma = 0
media = 0
total = 0
min = -1
max = 12

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "S":
    for x in range(12):
        max -= 1
        min += 1
        for y in range(12):
           if (y > min) and (y < max):
               soma += float(matriz[x][y])
    print("%.1f"%soma)
else:
    for x in range(12):
        max -= 1
        min += 1
        for y in range(12):
            if (y > min) and (y < max):
                media += float(matriz[x][y])
                total += 1
    media = media/total
    print("%.1f"%media)
