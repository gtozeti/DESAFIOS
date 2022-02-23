n1_, n2_ = input().split()
a = []
M = int(n1_)
N = int(n2_)

while M > 0 and N > 0:
    numeros = [M, N]
    n_ordenados = sorted(numeros)
    for x in range(n_ordenados[0], n_ordenados[1]+1):
        a.append(x)
    print(*a,"Sum=%i"%(sum(a)))
    a = []
    n1_, n2_ = input().split()
    M = int(n1_)
    N = int(n2_)
