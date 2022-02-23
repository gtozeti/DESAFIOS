x_,y_ = input().split()
x = int(x_)
y = int(y_)

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("quarto")
    x_, y_ = input().split()
    x = int(x_)
    y = int(y_)
