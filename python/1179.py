def imprimir(texto,vetor):
    for i,num in enumerate(vetor):
        print(texto+"[{}] = {}".format(i,num))
par = []
impar = []
for i in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            imprimir("par",par)
            par = []
    else:
        impar.append(num)
        if len(impar) == 5:
            imprimir("impar",impar)
            impar = []
imprimir("impar",impar)
imprimir("par",par)

    

