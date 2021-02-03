digito = int(input())
mes = ['January','February','March','April','May','June','July','August','September','October','November','December']

a = 0

for x in range(1,13):
    a += 1
    if x == digito:
        print(mes[a-1])
        break
