matriz = []
bin_ = ['---','--*','-*-','-**','*--','*-*','**-','***']
corvo = 0
soma = 0

while corvo != 3:
    matriz.append(input())
    if matriz[len(matriz)-1] == 'caw caw':
        corvo += 1


for x in range(len(matriz)):
    numero = matriz[x]

    if numero != 'caw caw':
        for y in range(8):
            bin_2 = bin_[y]
            if numero == bin_2:
                soma += y

    else:
        print(soma)
        soma = 0
