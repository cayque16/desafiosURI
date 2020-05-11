import string
alfabeto = list(string.ascii_letters)

casos = int(input())
for n in range(casos):
    entrada = input()
    saida = ''
    # PRIMEIRA ALTERACAO
    for i in entrada:
        if i in alfabeto:
            saida += chr(ord(i)+3)
        else:
            saida += i
    #SEGUNDA ALTERACAO
    saida = saida[::-1]
    # TERCEIRA ALTERACAO
    metade = (len(saida)//2)
    saida_final = ''
    for i in saida[metade:]:
        saida_final += chr(ord(i)-1)

    print(saida[:metade]+saida_final)