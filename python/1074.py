casos = int(input())

result = ''
for i in range(casos):
    num = int(input())
    if num == 0:
        print("NULL")
        continue
    elif num > 0:
        result = 'POSITIVE'
    else:
        result = 'NEGATIVE'
    if num % 2 == 0:
        print('EVEN '+result)
    else:
        print('ODD '+result)
    result = ''
    