A1,B1 = input().split(" ")
A = int(A1)
B = int(B1)

preco = [4.00,4.50,5.00,2.00,1.50]
total = preco[A-1]*B

print ("Total: R$ %.2f"%(total))
