n = int(input())
j1 = []
j2 = []

for x in range(n):
    j1.append(input())
    j2.append(input())

for x in range(n):
    if j1[x] == "pedra":
        if j2[x] == "papel":
            print("Jogador 1 venceu")
        elif j2[x] == "pedra":
            print("Sem ganhador")
        else:
            print("Jogador 2 venceu")
    elif j1[x] == "papel":
        if j2[x] == "papel":
            print("Ambos venceram")
        elif j2[x] == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Jogador 2 venceu")
    elif j1[x] == "ataque":
        if j2[x] == "papel":
            print("Jogador 1 venceu")
        elif j2[x] == "pedra":
            print("Jogador 1 venceu")
        else:
            print("Aniquilacao mutua")
