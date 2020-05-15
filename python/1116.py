for i in range(int(input())):
    x,y = map(int,input().split(" "))
    try:
        print("{:.1f}".format(x/y))
    except:
        print("divisao impossivel")