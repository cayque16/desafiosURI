while True:
    try:
        quant = int(input())
        nums = list(map(int,input().split(" ")))
        maior = max(nums)
        if maior < 10:
            print('1')
        elif maior < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break