nome = input()
salario = float(input())
vendas = float(input())

total = salario + (vendas*.15)

print("TOTAL = R$","%.2f" % total)
