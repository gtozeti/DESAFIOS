n = int(input())
a = []
soma = 0
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        row[j] = float(row[j])
    a.append(row)

for l in range(n):
    x = ((a[l][0] * 2) + (a[l][1] * 3) + (a[l][2] * 5)) / 10
    print("%.1f" % x)
