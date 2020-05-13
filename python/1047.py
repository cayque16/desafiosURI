h_inicio,m_inicio,h_fim,m_fim = map(int,input().split(" "))

total_inicio = h_inicio * 60 + m_inicio
total_fim = h_fim * 60 + m_fim

if total_inicio == total_fim:
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif total_fim > total_inicio:
  dif = total_fim - total_inicio
  horas = dif//60
  minutos = dif-horas*60
  print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas,minutos))
else:
  total = 24*60-total_inicio+total_fim
  horas = total//60
  minutos = total-horas*60
  print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas,minutos))
