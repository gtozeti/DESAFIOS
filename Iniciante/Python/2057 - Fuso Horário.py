s_,t_,f_ = input().split()
total = 0

s = int(s_)
t = int(t_)
f = int(f_)

soma = s+t+f

if soma > 24:
    total = soma - 24
    print(total)
elif soma < 0:
    total = 24 + soma
    print(total)
elif soma > 0 and soma < 24:
    print(soma)
else:
    print(0)
