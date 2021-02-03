n = int(input())
num = []

for x in range(n):
    num.append(int(input()))

for x in range(n):
    if num[x] % 2 == 0:
        print(0)
    else:
        print(1)
