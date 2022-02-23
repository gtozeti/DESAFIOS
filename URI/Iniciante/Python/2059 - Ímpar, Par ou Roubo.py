matriz = input().split()

if matriz[3] == '1' and matriz[4] == '1':
    print("Jogador 2 ganha!")

elif matriz[3] == '1' and matriz[4] == '0':
    print("Jogador 1 ganha!")

elif matriz[3] == '0' and matriz[4] == '1':
    print("Jogador 1 ganha!")

else:
    if matriz[0] == '1':
        soma = int(matriz[1]) + int(matriz[2])
        if soma % 2 == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        soma = int(matriz[1]) + int(matriz[2])
        if soma % 2 != 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
