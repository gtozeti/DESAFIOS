a_,b_ = input().split()

a = int(a_)
b = int(b_)

r = a%abs(b)
q = int((-r + a) / b)

print(q,r)
