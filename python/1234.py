MAIUSCULAS_ASCII = list(range(97,123))
MINUSCULAS_ASCII = list(range(65,91))
DIST_MAIUS_MINU_ASCII = 32

def sentenca_dancante(palavra):
    result = ''
    maiusculo = True
    for letra in palavra:
        if letra == ' ':
            result += ' '
            continue
        cod_ascii = ord(letra)
        if maiusculo:
            if cod_ascii in MINUSCULAS_ASCII:
                result += letra
            else:
                result += chr(cod_ascii - DIST_MAIUS_MINU_ASCII)
        else:
            if cod_ascii in MAIUSCULAS_ASCII:
                result += letra
            else:
                result += chr(cod_ascii + DIST_MAIUS_MINU_ASCII)
        maiusculo = not maiusculo
    return result
while True:
    try:
        sentencas = input().split("\n")
        for palavra in sentencas:
            print(sentenca_dancante(palavra))
    except EOFError:
        break