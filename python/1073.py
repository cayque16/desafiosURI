num = int(input())

for i in range(1,num+1):
    if i % 2 == 0:
        print("{}^{} = {}".format(i,2,i**2))