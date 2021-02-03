operacao = input()
matriz = []
soma = 0
media = 0
total = 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "S":
    for x in range(11):
        for y in range(1,12):
           if y > x:
               soma += float(matriz[x][y])
    print("%.1f"%soma)
else:
    for x in range(11):
        for y in range(1, 12):
            if y > x:
                media += float(matriz[x][y])
                total += 1
    media = media/total
    print("%.1f"%media)
