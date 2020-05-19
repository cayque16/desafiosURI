casos = int(input())
for i in range(casos):
    num = int(input())
    soma = 0
    for j in range(2,num+1):
        if num % j == 0:
            soma += 1
        if soma > 1:
            break
    if soma > 1:
        print("{} nao eh primo".format(num))
    else:
        print("{} eh primo".format(num))