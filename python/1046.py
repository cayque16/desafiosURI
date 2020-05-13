inicio, fim = map(int,input().split(" "))

if inicio == fim:
  print("O JOGO DUROU 24 HORA(S)")
elif fim > inicio:
  print("O JOGO DUROU {} HORA(S)".format(fim-inicio))
else:
  print("O JOGO DUROU {} HORA(S)".format(24-inicio+fim))
