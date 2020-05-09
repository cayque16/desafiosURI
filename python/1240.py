casos = int(input())
for i in range(casos):
  texto1,texto2 = input().split(" ")
  pos_texto2_in_texto1 = len(texto1)-len(texto2)
#   print(texto1[tam_texto2:])
  if texto2 == texto1[pos_texto2_in_texto1:]:
    print('encaixa')
  else:
    print('nao encaixa')

# 0123456    01234
# 5678690->7 78690->5
#   78690