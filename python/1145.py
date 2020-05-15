x,y = map(int,input().split(" "))

result = ''
for i in range(1,y+1):
    result += str(i)+' '
    if i % x == 0:
        result = result.strip()+'\n'
print(result.strip())