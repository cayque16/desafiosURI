casos = int(input())

for i in range(casos):
    x,y = map(int,input().split(" "))
    if x % 2 != 0:
        j = x
    else:
        j = x+1
    soma = j
    cont = 1
    while True:
        if cont == y:
            break
        j += 1
        if j % 2 != 0:
            cont += 1
            soma += j
    print(soma)