romano_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 2, 1]
romano_let = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "II", "I"]
n = int(input())
alg = ''

for x in range(len(romano_num)):
    while n >= romano_num[x]:
            n -= romano_num[x]
            alg += romano_let[x]

print(alg)
