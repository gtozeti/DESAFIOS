N = int(input())
numero = []

in_ = 0
out_ = 0

for i in range(N):
  numero.append(int(input()))
  
for a in numero:
    if a >= 10 and a <=20:
        in_ += 1

out_ = N - in_
print("%i in"%in_)
print("%i out"%out_)
