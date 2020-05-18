n = int(input())
result = '0 '
num1,num2,fib = 0,1,0
for i in range(n-1):
    temp = fib
    fib = num1 + num2
    num1,num2 = temp,fib
    result += str(fib)+' '
print(result.strip())