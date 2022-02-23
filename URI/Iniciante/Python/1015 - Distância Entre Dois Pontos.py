x_1,y_1 = input().split(" ")
x_2,y_2 = input().split(" ")

x1 = float(x_1)
y1 = float(y_1)
x2 = float(x_2)
y2 = float(y_2)

d0 = (((x2-x1)**2) + ((y2-y1)**2))
d = d0 ** 0.5

print("%.4f" % d)
