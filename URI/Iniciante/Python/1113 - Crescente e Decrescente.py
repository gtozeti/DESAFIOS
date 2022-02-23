n1_, n2_ = input().split()
M = int(n1_)
N = int(n2_)

while M != N:
    if M > N:
        print("Decrescente")
    else:
        print("Crescente")
    n1_, n2_ = input().split()
    M = int(n1_)
    N = int(n2_)
