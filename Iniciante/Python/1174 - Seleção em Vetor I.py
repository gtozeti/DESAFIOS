testes = []
for x in range(100):
    testes_ = input().split()
    testes.append(testes_)

for y in range(100):
    b = float(testes[y][0])
    if b <= 10:
        print("A[%i] = %.1f"%(y,b))
