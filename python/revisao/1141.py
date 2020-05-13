# CORRIGIR
# 	Time limit exceeded
while True:
    casos = int(input())
    if casos == 0:
        break
    lista = []
    for i in range(casos):
        lista.append(input())
    lista.sort(key=lambda item: len(item))

    lista_final = []
    lista_temp = []
    for i in range(len(lista)):
        lista_temp.append(lista[0])
        for j in lista:
            item_atual = lista_temp[-1]
            if item_atual == j:
                pass
            elif item_atual in j:
                lista_temp.append(j)
        lista_final.append(lista_temp)
        lista_temp = []

    maior = 0
    for i in lista_final:
        if maior < len(i):
            maior = len(i)
    print(maior)