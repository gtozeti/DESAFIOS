coluna1 = str(input())
coluna2 = str(input())
coluna3 = str(input())

vert1 = ["ave","mamifero"]
vert2 = ["carnivoro","onivoro","herbivoro"]
vert3 = ["aguia","pomba","homem","vaca"]
invert1 = ["inseto","anelideo"]
invert2 = ["herbivoro","hematofago","onivoro"]
invert3 = ["lagarta","pulga","sanguessuga","minhoca"]

a = 0
b = 0
c = 0
d = 0

if coluna1 == "vertebrado":
    for q in vert1:
        a += 1
        if coluna2 == q:
            break
    for w in vert2:
        b += 1
        if coluna3 == w:
            break
    
    soma = (a + b) - 2
    print(vert3[soma])

else:
    for e in invert1:
        c += 1
        if coluna2 == e:
          break
    for r in invert2:
        d += 1
        if coluna3 == r:
            break
    
    soma = (c + d) - 2
    print(invert3[soma])
