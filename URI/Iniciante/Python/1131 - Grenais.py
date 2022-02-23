inter_,gremio_ = input().split()
inter = int(inter_)
gremio = int(gremio_)

a = 0
contador = 1

v_inter = 0
v_gremio = 0
empate = 0

if inter > gremio:
    v_inter += 1
elif inter == gremio:
    empate += 1
else:
    v_gremio += 1



while a == 0:
    print("Novo grenal (1-sim 2-nao)")
    cond = int(input())
    if cond == 2:
        a = 1
    else:
        inter_ = 0
        gremio_ = 0
        inter = 0
        gremio = 0
        inter_, gremio_ = input().split()
        inter = int(inter_)
        gremio = int(gremio_)
        contador += 1
        if inter > gremio:
            v_inter += 1
        elif inter == gremio:
            empate += 1
        else:
            v_gremio += 1

print("%i grenais"%contador)
print("Inter:%i"%v_inter)
print("Gremio:%i"%v_gremio)
print("Empates:%i"%empate)
if inter > gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
