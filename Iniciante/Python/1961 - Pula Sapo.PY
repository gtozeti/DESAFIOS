altura_, canos_ = input().split()

altura = int(altura_)
canos = int(canos_)
cond = 0

fase = input().split()

for x in range(canos-1):
    a = int(fase[x])
    b = int(fase[x+1])
    if abs(a - b) <= altura:
        cond += 1

if cond == (canos - 1):
    print("YOU WIN")
else:
    print("GAME OVER")
