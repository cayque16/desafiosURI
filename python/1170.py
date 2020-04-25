n = int(input())

entradas = []
for i in range(1,n+1):
	entradas.append(float(input()))
j=0
for i in entradas:
	valor = i
	while (valor > 1):
		valor /= 2
		j += 1
	print("{} dias".format(j))
	j=0