soma,cont = 0,0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    cont += 1
print("{:.2f}".format(soma/cont))