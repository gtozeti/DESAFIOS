n = int(input())
matriz = []
caso = 0

for x in range(n):
    matriz_ = input().split()
    matriz.append(matriz_)

for x in range(n):
    c1 = matriz[x][0]
    c2 = matriz[x][1]

    caso += 1

    if c1 == 'pedra':
        if c2 == 'papel' or c2 == 'Spock':
            print("Caso #%i: Raj trapaceou!"% caso)
        elif c1 == c2:
            print("Caso #%i: De novo!" % caso)
        else:
            print("Caso #%i: Bazinga!" % caso)

    elif c1 == 'papel':
        if c2 == 'tesoura' or c2 == 'lagarto':
            print("Caso #%i: Raj trapaceou!"% caso)
        elif c1 == c2:
            print("Caso #%i: De novo!" % caso)
        else:
            print("Caso #%i: Bazinga!" % caso)

    elif c1 == 'tesoura':
        if c2 == 'Spock' or c2 == 'pedra':
            print("Caso #%i: Raj trapaceou!"% caso)
        elif c1 == c2:
            print("Caso #%i: De novo!" % caso)
        else:
            print("Caso #%i: Bazinga!" % caso)

    elif c1 == 'lagarto':
        if c2 == 'pedra' or c2 == 'tesoura':
            print("Caso #%i: Raj trapaceou!"% caso)
        elif c1 == c2:
            print("Caso #%i: De novo!" % caso)
        else:
            print("Caso #%i: Bazinga!" % caso)

    elif c1 == 'Spock':
        if c2 == 'lagarto' or c2 == 'papel':
            print("Caso #%i: Raj trapaceou!"% caso)
        elif c1 == c2:
            print("Caso #%i: De novo!" % caso)
        else:
            print("Caso #%i: Bazinga!" % caso)
