n = int(input())
nomes = []
num = []
for x in range(n):
    nomes_ = input().split()
    nomes.append(nomes_)
    num_ = input().split()
    num.append(num_)

for x in range(n):
    if (int(num[x][0]) + int(num[x][1])) % 2 == 0:
        for y in range(4):
            if nomes[x][y] == "PAR":
                print(nomes[x][y-1])
    else:
        for y in range(4):
            if nomes[x][y] == "IMPAR":
                print(nomes[x][y-1])
