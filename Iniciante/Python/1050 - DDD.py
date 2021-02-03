digito = int(input())
ddd = [61,71,11,21,32,19,27,31]
cidade = ['Brasilia','Salvador','Sao Paulo','Rio de Janeiro','Juiz de Fora','Campinas','Vitoria','Belo Horizonte']

a = 0

for x in ddd:
    a += 1
    if x == digito:
        print(cidade[a-1])
        break
    elif x != digito  and a == 8:
        print("DDD nao cadastrado")
