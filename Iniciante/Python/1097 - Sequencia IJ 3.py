i = 3
for y in range(1,10,2):
    i += 2
    for x in reversed(range(i, i+3, 1)):
        print("I=%i J=%i" %(y, x))
