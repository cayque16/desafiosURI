cont,soma = 0,0
while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
        continue
    cont += 1
    soma += nota
    if cont == 2:
        print("media = {:.2f}".format(soma/2))
        soma = 0
        cont = 0
    else:
        continue
    op = ''
    while True:
        op = input("novo calculo (1-sim 2-nao)\n")
        if op in ['1','2']:
            break
    if op == '2':
        break
    
