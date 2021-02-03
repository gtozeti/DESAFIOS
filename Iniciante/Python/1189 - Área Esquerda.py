operacao = input()
matriz = []
soma = 0
media = 0
total = 0
max = -1

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "S":
    for x in range(12):
        if x > 6:
            max -= 1
        elif x == 6:
            max = 5
        else:
            max += 1
        for y in range(5):
           if y < max:
               soma += float(matriz[x][y])
    print("%.1f"%soma)
else:
    for x in range(12):
        if x > 6:
            max -= 1
        elif x == 6:
            max = 5
        else:
            max += 1
        for y in range(5):
            if y < max:
                media += float(matriz[x][y])
                total += 1
    media = media/total
    print("%.1f"%media)
