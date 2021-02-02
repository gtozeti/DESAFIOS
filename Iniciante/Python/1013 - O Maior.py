a_1,b_1,c_1 = input().split(" ")

a = int(a_1)
b = int(b_1)
c = int(c_1)

m = (a+b+abs(a-b))/2
maior = int((m+c+abs(m-c))/2)

print(maior,"eh o maior")
