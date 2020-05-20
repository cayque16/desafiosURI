tam = 12
coluna = int(input())
op = input()
soma = 0
for i in range(tam):
    for j in range(tam):
        num = float(input())
        if j == coluna:
            soma += num
if op == 'S':
  print(soma)
elif op == 'M':
  print("{:.1f}".format(soma/tam))