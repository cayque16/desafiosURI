x = int(input())
y = int(input())

if x > y:
    temp = x
    x = y
    y = temp

for i in range(x+1,y):
    resto = i % 5
    if resto in [2,3]:
        print(i)