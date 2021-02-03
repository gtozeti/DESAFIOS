a_, b_, c_ = input().split()

a = int(a_)
b = int(b_)
c = int(c_)

if (a > b and c >= b) or (b > a and (c-b) >= (b-a)) or (b < a and (b-c) < (a-b)) or (a == b and c > b):
    print(":)")
else:
    print(":(")
