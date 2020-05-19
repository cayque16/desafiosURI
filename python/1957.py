def num_to_hexa(num: int) -> str:
    letras = ['A','B','C','D','E','F']

    if num < 10:
        return str(num)
    else:
        return letras[num-10]

num = int(input())

if num < 16:
    print(num_to_hexa(num))
else:
    result = ''
    while num > 15:
        resto = num % 16
        num = num // 16
        if resto < 16:
            resto = num_to_hexa(resto)
        result = resto + result
    
    print(num_to_hexa(num)+result)