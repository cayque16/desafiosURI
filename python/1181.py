tam = 12
linha = int(input())
op = input()
soma = 0
for i in range(tam):
    for j in range(tam):
        num = float(input())
        if i == linha:
            soma += num
if op == 'S':
  print(soma)
elif op == 'M':
  print("{:.1f}".format(soma/tam))