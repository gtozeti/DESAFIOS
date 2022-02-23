a_, b_ = input().split()

a = float(a_)
b = float(b_)

porc = ((b * 100)/a) - 100

print("%.2f%%" % porc)
