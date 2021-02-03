salario = float(input())
result  = 0

if salario >= 0 and salario <= 2000.00:
    print("Isento")
else:
    if salario > 2000.00 and salario <= 3000.00:
        result = (salario-2000.00)*0.08
    elif salario > 3000.01 and salario <= 4500.00:
        result = (salario-3000.00)*0.18 + (1000.00)*0.08
    elif salario > 4500.00:
        result = (salario-4500.00)*0.28 +(1500.00)*0.18+ (1000.00)*0.08
    print("R$ %.2f"%(result))
