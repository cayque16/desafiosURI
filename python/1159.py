while True:
    num = int(input())
    if num == 0:
        break
    soma,cont = 0,0
    for i in range(num,num+10):
        if i % 2 == 0:
            soma += i
            cont += 1
        if cont == 5:
            break
    print(soma)