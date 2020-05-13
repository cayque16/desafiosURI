num1,num2 = map(int,input().split(" "))

if num1 > num2:
    if num1 % num2 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif num1 < num2:
    if num2 % num1 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    print("Sao Multiplos")