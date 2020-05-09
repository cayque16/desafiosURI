casos = int(input())
for i in range(casos):
  texto1,texto2 = input().split(" ")
  x = texto1.find(texto2)
  if x >= 0:
    print('encaixa')
  else:
    print('nao encaixa')