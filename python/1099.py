for i in range(int(input())):
    x,y = map(int,input().split(" "))
    if y < x:
        temp = y
        y = x
        x = temp
    soma = 0
    for j in range(x+1,y):
        if j % 2 != 0:
            soma += j
    print(soma)
    soma = 0