a_1,b_1,c_1 = input().split(" ")

a = float(a_1)
b = float(b_1)
c = float(c_1)

a1 = float (a*c/2)
b1 = float (3.14159*c **2)
c1 = float ((a+b)*c/2)
d1 = float (b*b)
e1 = float (a*b)

print("TRIANGULO:","%.3f" % a1)
print("CIRCULO:","%.3f" % b1)
print("TRAPEZIO:","%.3f" % c1)
print("QUADRADO:","%.3f" % d1)
print("RETANGULO:","%.3f" % e1)
