tam = 12
op = input()
soma,cont = 0,0
for i in range(tam):
  for j in range(tam):
    num = float(input())
    if i > j:
        soma += num
        cont += 1

if op == 'S':
  print(soma)
elif op == 'M':
  print("{:.1f}".format(soma/cont))