from asyncio.windows_events import NULL


n = 6
lista = list()
for x in range(1000,10000):
   
    m = x // 1000
    c = (x - (m * 1000))//100
    d = (x - (m * 1000) - (c* 100))//10
    u = (x - (m * 1000) - (c* 100) - (d* 10))
    if ((m <= n and c <= n and d <= n and u <= n) and ((m+c+d+u) == 21)):
            lista.append(x)
print(None)
