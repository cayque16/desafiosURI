x = int(input())
cont,y = 1,x
soma,i = x,x
while True:
    if y <= x:
        y = int(input())
        continue
    i += 1
    soma += i
    cont += 1
    if soma >= y:
        break
print(cont)