soma = 0
cont = 0
while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        cont += 1
        soma += nota
        if cont == 2:
            print("media = {:.2f}".format(soma/2))
            break
