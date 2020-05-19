casos = int(input())
for i in range(casos):
    pa,pb,ga,gb = map(float,input().split(" "))

    cont = 0
    while pa <= pb:
        pa += int(pa * ga/100)
        pb += int(pb * gb/100)
        cont += 1
        if cont > 100:
            break
    if cont <= 100:
        print("{} anos.".format(cont))
    else:
        print("Mais de 1 seculo.")