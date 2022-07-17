while True:
    try:
        ano = input()
        if len(ano) < 3:
            print(1)
        elif len(ano) == 3:
            if ano[-1] == '0':
                print(ano[0])
            else:
                print(int(ano[0])+1)
        else:
            if ano[-2]+ano[-1] == '00':
                print(ano[0]+ano[1])
            else:
                print(int(ano[0]+ano[1])+1)
    except EOFError:
        break