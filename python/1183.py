tam = 12
op = input()
soma,cont = 0,0
for i in range(tam):
  for j in range(tam):
    num = float(input())
    if i < j:
        cont +=  1
        soma += num

if op == 'S':
  print(soma)
elif op == 'M':
  print("{:.1f}".format(soma/cont))