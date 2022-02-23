n = int(input())
casos = input().split()

for i in range(n):
    casos[i] = int(casos[i])

min_ = min(casos)
print(casos.index(min_) + 1)
