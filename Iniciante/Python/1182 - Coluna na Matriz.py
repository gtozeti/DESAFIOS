nlinha = int(input())
operacao = input()
matriz = []
soma = 0
media = 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "S":
    for x in range(12):
        soma += float(matriz[x][nlinha])
    print("%.1f"%soma)
else:
    for x in range(12):
        media += float(matriz[x][nlinha])
    media = media/12
    print("%.1f"%media)
