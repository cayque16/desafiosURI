while True:
    m,n = map(int,input().split(" "))
    if m <= 0 or n <= 0:
        break
    if m > n:
        temp = m
        m = n
        n = temp
    result = ''
    soma = 0
    for i in range(m,n+1):
        result += str(i) + ' '
        soma += i
    print(result+"Sum={}".format(soma))
    soma = 0
    result = ''