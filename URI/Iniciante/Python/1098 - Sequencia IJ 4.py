i = -0.2
a = 0.8
b = 1.8
c = 2.8

for y in range(0, 11):
    i += 0.2
    a += 0.2
    b += 0.2
    c += 0.2
    a = round(a, 1)
    b = round(b, 1)
    c = round(c, 1)
    i = round(i, 1)

    if (a == 1 or a == 2 or a == 3) and (i == 0 or i == 1 or i == 2):
        a = int(a)
        b = int(b)
        c = int(c)
        i = int(i)
        print("I=%i J=%i" % (i, a))
        print("I=%i J=%i" % (i, b))
        print("I=%i J=%i" % (i, c))

    elif a == 1 or a == 2 or a == 3:
        a = int(a)
        b = int(b)
        c = int(c)
        print("I=%.1f J=%i" % (i, a))
        print("I=%.1f J=%i" % (i, b))
        print("I=%.1f J=%i" % (i, c))

    elif i == 0 or i == 1 or i == 2:
        i = int(i)
        print("I=%i J=%.1f" % (i, a))
        print("I=%i J=%.1f" % (i, b))
        print("I=%i J=%.1f" % (i, c))

    else:
        print("I=%.1f J=%.1f" % (i, a))
        print("I=%.1f J=%.1f" % (i, b))
        print("I=%.1f J=%.1f" % (i, c))
