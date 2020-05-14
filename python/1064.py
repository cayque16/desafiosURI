soma = 0
cont = 0
for i in range(6):
    num = float(input())
    if num > 0:
        soma += num
        cont += 1
print("{} valores positivos".format(cont))
print("{:.1f}".format(soma/cont))