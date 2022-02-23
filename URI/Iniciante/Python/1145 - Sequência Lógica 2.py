x_,y_ = input().split()
x = int(x_)
y = int(y_)
a = []
b = 0

for i in range(1,y+1):
    row = i
    a.append(row)

while b < y:
    for k in range(x):
        if b == y:
            break
        else:
            if k == (x-1):

                print(a[b], end='')
            else:
                print(a[b], end=' ')

            b += 1
    if b < y:
        print()
