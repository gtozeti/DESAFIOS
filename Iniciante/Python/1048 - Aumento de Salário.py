a = float(input())

if a <= 400.00:
    salario = a + a * .15
    reajuste = salario - a
    print("Novo salario: %.2f"%(salario))
    print("Reajuste ganho: %.2f"%(reajuste))
    print("Em percentual: 15 %")
elif a > 400.00 and a <= 800.00 :
    salario = a + a * .12
    reajuste = salario - a
    print("Novo salario: %.2f"%(salario))
    print("Reajuste ganho: %.2f"%(reajuste))
    print("Em percentual: 12 %")
elif a > 800.00 and a <= 1200.00 :
    salario = a + a * .10
    reajuste = salario - a
    print("Novo salario: %.2f"%(salario))
    print("Reajuste ganho: %.2f"%(reajuste))
    print("Em percentual: 10 %")
elif a > 1200.00 and a <= 2000.00 :
    salario = a + a * .07
    reajuste = salario - a
    print("Novo salario: %.2f"%(salario))
    print("Reajuste ganho: %.2f"%(reajuste))
    print("Em percentual: 7 %")
else:
    salario = a + a * .04
    reajuste = salario - a
    print("Novo salario: %.2f"%(salario))
    print("Reajuste ganho: %.2f"%(reajuste))
    print("Em percentual: 4 %")
